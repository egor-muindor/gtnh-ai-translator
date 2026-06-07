/* GTNH Questbook Translation Review — vanilla JS, offline, single-quest review tool */
(function () {
  "use strict";

  // ---------- State ----------
  var ALL = [];          // raw records from review_data.json
  var DECK = [];         // current filtered list of records
  var idx = 0;           // index into DECK
  var rendered = true;   // RENDERED vs RAW toggle
  var ratings = loadRatings();
  var LS_KEY = "gtnh_review_ratings_v1";

  // ---------- DOM ----------
  var $ = function (id) { return document.getElementById(id); };
  var cardEl = $("card");
  var progressEl = $("progress");
  var gotoInput = $("gotoInput");
  var gotoTotal = $("gotoTotal");
  var ratingCounterEl = $("ratingCounter");

  // ---------- Boot ----------
  function init() {
    bindUI();
    fetch("review_data.json", { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        ALL = Array.isArray(data) ? data : [];
        buildCategoryFilter();
        applyFilters(true);
        updateRatingCounter();
      })
      .catch(function (err) {
        cardEl.innerHTML =
          '<div class="empty-state"><h2>Не удалось загрузить review_data.json</h2>' +
          '<p>Запустите через локальный сервер: <code>python3 -m http.server 8765</code></p>' +
          '<p style="color:var(--text-faint)">' + escapeHtml(String(err)) + "</p></div>";
      });
  }

  // ---------- Filters ----------
  function buildCategoryFilter() {
    var set = {};
    ALL.forEach(function (q) {
      ["name", "desc"].forEach(function (f) {
        var v = q[f];
        if (v && v.changed && v.category) set[v.category] = true;
      });
    });
    var cats = Object.keys(set).sort();
    var sel = $("filterCategory");
    sel.innerHTML = '<option value="">Любая категория</option>';
    cats.forEach(function (c) {
      var o = document.createElement("option");
      o.value = c; o.textContent = c;
      sel.appendChild(o);
    });
  }

  function currentFilters() {
    return {
      q: $("search").value.trim().toLowerCase(),
      category: $("filterCategory").value,
      severity: $("filterSeverity").value,
      field: $("filterField").value,
      rating: $("filterRating").value,
      hasOld: $("filterHasOld").checked
    };
  }

  // A record passes if at least one of its CHANGED fields (respecting field filter) matches.
  function recordMatches(q, f) {
    var fields = f.field ? [f.field] : ["name", "desc"];
    var anyChangedFieldConsidered = false;
    var fieldMatch = false;

    for (var i = 0; i < fields.length; i++) {
      var v = q[fields[i]];
      if (!v || !v.changed) continue;
      anyChangedFieldConsidered = true;
      if (f.category && v.category !== f.category) continue;
      if (f.severity && v.severity !== f.severity) continue;
      if (f.hasOld && !(v.old && v.old.length)) continue;
      if (f.q) {
        var hay = ((v.en || "") + "\n" + (v.old || "") + "\n" + (v.new || "")).toLowerCase();
        if (hay.indexOf(f.q) === -1) continue;
      }
      fieldMatch = true;
      break;
    }
    if (!anyChangedFieldConsidered) return false;
    if (!fieldMatch) return false;

    // Rating filter is per-quest.
    if (f.rating) {
      var r = ratings[q.questId];
      if (f.rating === "unrated") { if (r && (r.rating || (r.note && r.note.length))) return false; }
      else if (f.rating === "note") { if (!(r && r.note && r.note.length)) return false; }
      else { if (!(r && r.rating === f.rating)) return false; }
    }
    return true;
  }

  function applyFilters(keepIfPossible) {
    var f = currentFilters();
    var prevId = (keepIfPossible && DECK[idx]) ? DECK[idx].questId : null;
    DECK = ALL.filter(function (q) { return recordMatches(q, f); });

    idx = 0;
    if (prevId) {
      for (var i = 0; i < DECK.length; i++) {
        if (DECK[i].questId === prevId) { idx = i; break; }
      }
    }
    gotoTotal.textContent = "/ " + DECK.length;
    gotoInput.max = DECK.length;
    render();
  }

  // ---------- Navigation ----------
  function go(delta) {
    if (!DECK.length) return;
    idx = Math.min(DECK.length - 1, Math.max(0, idx + delta));
    render();
  }
  function gotoNum(n) {
    if (!DECK.length) return;
    n = Math.min(DECK.length, Math.max(1, n | 0));
    idx = n - 1;
    render();
  }

  // ---------- Render card ----------
  function render() {
    progressEl.textContent = DECK.length ? (idx + 1) + " / " + DECK.length : "0 / 0";
    gotoInput.value = DECK.length ? (idx + 1) : "";
    $("prevBtn").disabled = $("prevBtn2").disabled = idx <= 0;
    $("nextBtn").disabled = $("nextBtn2").disabled = idx >= DECK.length - 1;

    if (!DECK.length) {
      cardEl.innerHTML = '<div class="empty-state"><h2>Нет записей под текущие фильтры</h2>' +
        '<p>Измените или сбросьте фильтры.</p></div>';
      return;
    }

    var q = DECK[idx];
    var r = ratings[q.questId] || {};
    var card = document.createElement("div");
    card.className = "card";

    // Head: ids + rating controls
    var head = document.createElement("div");
    head.className = "card-head";
    var left = document.createElement("div");
    left.innerHTML = '<div class="card-id">' + escapeHtml(q.questId) + '</div>' +
      '<div class="card-base">' + escapeHtml(q.base || "") + '</div>';
    head.appendChild(left);
    head.appendChild(buildRating(q, r));
    card.appendChild(head);

    // Note area (toggled)
    var note = document.createElement("textarea");
    note.className = "note-area" + ((r.note && r.note.length) ? "" : " hidden");
    note.placeholder = "Заметка рецензента…";
    note.value = r.note || "";
    note.id = "noteArea";
    note.addEventListener("input", function () {
      setRating(q.questId, { note: note.value });
      updateRatingCounter();
      updateRateButtonStates(q.questId);
    });
    card.appendChild(note);

    // Fields
    ["name", "desc"].forEach(function (fname) {
      var v = q[fname];
      if (!v) return;
      card.appendChild(buildField(fname, v));
    });

    cardEl.innerHTML = "";
    cardEl.appendChild(card);
  }

  function buildRating(q, r) {
    var wrap = document.createElement("div");
    wrap.className = "rating";

    var ok = mkRateBtn("👍 OK", "ok");
    var bad = mkRateBtn("👎 Needs work", "bad");
    var noteBtn = mkRateBtn("✏️ Заметка", "note");

    ok.onclick = function () { toggleRating(q.questId, "ok"); };
    bad.onclick = function () { toggleRating(q.questId, "bad"); };
    noteBtn.onclick = function () {
      var ta = $("noteArea");
      if (ta) { ta.classList.toggle("hidden"); if (!ta.classList.contains("hidden")) ta.focus(); }
    };

    wrap.appendChild(ok);
    wrap.appendChild(bad);
    wrap.appendChild(noteBtn);
    wrap._refresh = function () {
      ok.className = "rate-btn" + (r2(q.questId, "rating") === "ok" ? " active-ok" : "");
      bad.className = "rate-btn" + (r2(q.questId, "rating") === "bad" ? " active-bad" : "");
      noteBtn.className = "rate-btn" + (r2(q.questId, "note") ? " has-note" : "");
    };
    wrap._refresh();
    wrap.dataset.qid = q.questId;
    return wrap;
  }

  function mkRateBtn(label, key) {
    var b = document.createElement("button");
    b.className = "rate-btn";
    b.textContent = label;
    b.dataset.key = key;
    return b;
  }

  function r2(qid, k) { var r = ratings[qid]; return r ? r[k] : undefined; }

  function updateRateButtonStates(qid) {
    var ratingWrap = document.querySelector('.rating[data-qid="' + cssEsc(qid) + '"]');
    if (ratingWrap && ratingWrap._refresh) ratingWrap._refresh();
  }

  function buildField(fname, v) {
    var field = document.createElement("div");
    field.className = "field" + (v.changed ? "" : " unchanged");

    var title = document.createElement("div");
    title.className = "field-title";
    title.innerHTML = "<span>" + (fname === "name" ? "Название (name)" : "Описание (desc)") + "</span>";
    if (!v.changed) {
      title.innerHTML += '<span class="tag unchanged-badge">не изменено</span>';
    }
    field.appendChild(title);

    // Metadata (only meaningful for changed fields)
    if (v.changed) {
      var meta = document.createElement("div");
      meta.className = "meta";
      meta.appendChild(tag("cat", v.category || "—"));
      meta.appendChild(tag("sev-" + (v.severity || ""), v.severity || "—"));
      meta.appendChild(tag("", "mode: " + (v.mode || "—")));
      field.appendChild(meta);

      if (v.reason) {
        var reason = document.createElement("div");
        reason.className = "reason";
        reason.innerHTML = '<span class="reason-label">Причина правки</span>' + escapeHtml(v.reason);
        field.appendChild(reason);
      }
    }

    // Versions
    var versions = document.createElement("div");
    versions.className = "versions" + (fname === "name" ? "" : " cols");

    versions.appendChild(verBlock("ver-en", "English (source)", renderContent(v.en || "")));

    var oldEmpty = !(v.old && v.old.length);
    versions.appendChild(verBlock("ver-old", "Старый перевод",
      oldEmpty ? '<span class="ver-empty">(нет старого перевода)</span>' : renderContent(v.old)));

    versions.appendChild(verBlock("ver-new", "Новый перевод",
      renderNewWithDiff(v.old || "", v.new || "")));

    field.appendChild(versions);
    return field;
  }

  function verBlock(cls, label, htmlContent) {
    var b = document.createElement("div");
    b.className = "ver " + cls;
    var bodyCls = "ver-body" + (rendered ? "" : " raw");
    b.innerHTML = '<div class="ver-head">' + escapeHtml(label) + "</div>" +
      '<div class="' + bodyCls + '">' + htmlContent + "</div>";
    return b;
  }

  function tag(cls, text) {
    var t = document.createElement("span");
    t.className = "tag " + cls;
    t.textContent = text;
    return t;
  }

  // ---------- Content rendering (Minecraft markup) ----------
  // In RAW mode: escape everything, show literal codes/tags.
  // In RENDERED mode: apply §codes, %n breaks, %% -> %, and [tag] markup.
  function renderContent(text) {
    if (!rendered) return escapeHtml(text);
    return mcRender(text);
  }

  // RAW mode: show literal new text (no diff). RENDERED mode: diff-highlighted + markup.
  function renderNewWithDiff(oldText, newText) {
    if (!rendered) return escapeHtml(newText);
    if (!oldText || !oldText.length) {
      // No baseline to diff against — whole thing is new but we still render markup.
      return mcRender(newText);
    }
    return mcRenderWithDiff(oldText, newText);
  }

  // Tokenize raw string into segments: text runs, color codes, breaks, markup tags.
  // Returns array of {type, value, code} preserving order.
  function tokenize(s) {
    var out = [];
    var i = 0, n = s.length;
    var buf = "";
    function flush() { if (buf) { out.push({ type: "text", value: buf }); buf = ""; } }
    while (i < n) {
      var ch = s[i];
      if (ch === "%") {
        var nx = s[i + 1];
        if (nx === "n") { flush(); out.push({ type: "break" }); i += 2; continue; }
        if (nx === "%") { buf += "%"; i += 2; continue; }
        buf += "%"; i += 1; continue;
      }
      if (ch === "§") { // §
        var code = s[i + 1];
        if (code !== undefined) { flush(); out.push({ type: "code", code: code.toLowerCase() }); i += 2; continue; }
        buf += ch; i += 1; continue;
      }
      if (ch === "[") {
        var m = /^\[(\/?)(note|warn|url|quest)\]/i.exec(s.slice(i));
        if (m) {
          flush();
          out.push({ type: "tag", close: m[1] === "/", name: m[2].toLowerCase() });
          i += m[0].length; continue;
        }
      }
      buf += ch; i += 1;
    }
    flush();
    return out;
  }

  // Active formatting state -> open span classes.
  function styleStateClasses(st) {
    var c = [];
    if (st.bold) c.push("mc-bold");
    if (st.italic) c.push("mc-italic");
    if (st.under && st.strike) c.push("mc-under-strike");
    else if (st.under) c.push("mc-underline");
    else if (st.strike) c.push("mc-strike");
    if (st.obf) c.push("mc-obf");
    return c;
  }

  var MC_COLORS = {
    "0": "#000000", "1": "#0000aa", "2": "#00aa00", "3": "#00aaaa",
    "4": "#aa0000", "5": "#aa00aa", "6": "#ffaa00", "7": "#aaaaaa",
    "8": "#555555", "9": "#5555ff", "a": "#55ff55", "b": "#55ffff",
    "c": "#ff5555", "d": "#ff55ff", "e": "#ffff55", "f": "#ffffff"
  };

  function freshState() { return { color: null, bold: false, italic: false, under: false, strike: false, obf: false }; }

  function applyCode(st, code) {
    if (code === "r") { return freshState(); }
    if (MC_COLORS[code]) { var ns = freshState(); ns.color = MC_COLORS[code]; return ns; }
    var s = cloneState(st);
    if (code === "l") s.bold = true;
    else if (code === "o") s.italic = true;
    else if (code === "n") s.under = true;
    else if (code === "m") s.strike = true;
    else if (code === "k") s.obf = true;
    return s;
  }
  function cloneState(st) { return { color: st.color, bold: st.bold, italic: st.italic, under: st.under, strike: st.strike, obf: st.obf }; }

  // Render a token stream into HTML. `wrapText(htmlEscapedText)` lets callers inject diff spans.
  function tokensToHtml(tokens, wrapText) {
    var html = "";
    var st = freshState();
    var openText = false;          // is a text-style span currently open?
    var blockStack = [];           // open [note]/[warn]/[url]/[quest] blocks

    function openTextSpan() {
      var cls = styleStateClasses(st);
      var styleAttr = st.color ? ' style="color:' + st.color + '"' : "";
      html += '<span class="' + cls.join(" ") + '"' + styleAttr + ">";
      openText = true;
    }
    function closeTextSpan() { if (openText) { html += "</span>"; openText = false; } }

    for (var i = 0; i < tokens.length; i++) {
      var t = tokens[i];
      if (t.type === "text") {
        if (!openText) openTextSpan();
        html += wrapText ? wrapText(escapeHtml(t.value)) : escapeHtml(t.value);
      } else if (t.type === "break") {
        closeTextSpan();
        html += "<br>";
      } else if (t.type === "code") {
        closeTextSpan();
        st = applyCode(st, t.code);
      } else if (t.type === "tag") {
        closeTextSpan();
        if (!t.close) {
          if (t.name === "note") { html += '<span class="mc-note">'; blockStack.push("note"); }
          else if (t.name === "warn") { html += '<span class="mc-warn">'; blockStack.push("warn"); }
          else if (t.name === "url") { html += '<span class="mc-url" data-url="1">'; blockStack.push("url"); }
          else if (t.name === "quest") { html += '<span class="mc-quest">'; blockStack.push("quest"); }
        } else {
          if (blockStack.length) { blockStack.pop(); html += "</span>"; }
        }
      }
    }
    closeTextSpan();
    while (blockStack.length) { blockStack.pop(); html += "</span>"; }
    return html;
  }

  function mcRender(text) {
    var html = tokensToHtml(tokenize(text), null);
    return linkifyUrls(html);
  }

  // Render NEW with word-level diff vs OLD. We diff the PLAIN visible text (codes/markup
  // stripped to their break semantics) then map diff status back onto the new token stream.
  function mcRenderWithDiff(oldText, newText) {
    var oldWords = plainWords(oldText);
    var newWords = plainWords(newText);
    var ops = diffWords(oldWords, newWords); // array of {type:'eq'|'add'|'del', word}

    // Build a per-new-word status list (only 'eq' and 'add' belong to NEW).
    var newStatus = [];   // status for each successive word in NEW
    var delQueue = [];     // removed words to show inline (red), keyed by position
    var pendingDel = [];
    ops.forEach(function (op) {
      if (op.type === "del") { pendingDel.push(op.word); }
      else if (op.type === "add") { newStatus.push({ s: "add", del: pendingDel.splice(0) }); }
      else { newStatus.push({ s: "eq", del: pendingDel.splice(0) }); }
    });
    var trailingDel = pendingDel.splice(0);

    // Now render newText tokens, wrapping each whitespace-delimited word with its status.
    var wordCursor = { i: 0 };
    function wrapText(escapedHtml) {
      // escapedHtml is HTML-escaped text. Split on whitespace but keep the whitespace.
      var parts = escapedHtml.split(/(\s+)/);
      var res = "";
      for (var k = 0; k < parts.length; k++) {
        var p = parts[k];
        if (p === "" ) continue;
        if (/^\s+$/.test(p)) { res += p; continue; }
        var stat = newStatus[wordCursor.i] || { s: "eq", del: [] };
        // emit any removed words that preceded this new word
        if (stat.del && stat.del.length) {
          res += '<span class="diff-del">' + stat.del.map(escapeHtml).join(" ") + "</span> ";
        }
        if (stat.s === "add") res += '<span class="diff-add">' + p + "</span>";
        else res += p;
        wordCursor.i++;
      }
      return res;
    }

    var html = tokensToHtml(tokenize(newText), wrapText);
    if (trailingDel.length) {
      html += ' <span class="diff-del">' + trailingDel.map(escapeHtml).join(" ") + "</span>";
    }
    return linkifyUrls(html);
  }

  // Convert raw string to a list of visible words (drop §codes, %n -> space, [tags] dropped).
  function plainWords(s) {
    var toks = tokenize(s);
    var plain = "";
    toks.forEach(function (t) {
      if (t.type === "text") plain += t.value;
      else if (t.type === "break") plain += " ";
      // codes & tags contribute nothing to word content
    });
    plain = plain.replace(/\s+/g, " ").trim();
    return plain.length ? plain.split(" ") : [];
  }

  // LCS-based word diff. Returns ordered ops.
  function diffWords(a, b) {
    var n = a.length, m = b.length;
    // Guard against pathological sizes (paragraphs are fine; cap to avoid huge tables).
    var CAP = 1200;
    if (n > CAP || m > CAP) {
      // Fallback: treat all of b as add, all of a as del (still correct, less granular).
      var fb = [];
      a.forEach(function (w) { fb.push({ type: "del", word: w }); });
      b.forEach(function (w) { fb.push({ type: "add", word: w }); });
      return fb;
    }
    // LCS DP table.
    var dp = new Array(n + 1);
    for (var i = 0; i <= n; i++) { dp[i] = new Int32Array(m + 1); }
    for (i = n - 1; i >= 0; i--) {
      for (var j = m - 1; j >= 0; j--) {
        if (a[i] === b[j]) dp[i][j] = dp[i + 1][j + 1] + 1;
        else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
      }
    }
    var ops = [];
    i = 0; j = 0;
    while (i < n && j < m) {
      if (a[i] === b[j]) { ops.push({ type: "eq", word: b[j] }); i++; j++; }
      else if (dp[i + 1][j] >= dp[i][j + 1]) { ops.push({ type: "del", word: a[i] }); i++; }
      else { ops.push({ type: "add", word: b[j] }); j++; }
    }
    while (i < n) { ops.push({ type: "del", word: a[i] }); i++; }
    while (j < m) { ops.push({ type: "add", word: b[j] }); j++; }
    return ops;
  }

  // Turn the inner text of [url] spans into anchors, and auto-link bare URLs inside mc-url spans.
  function linkifyUrls(html) {
    return html.replace(/<span class="mc-url" data-url="1">([\s\S]*?)<\/span>/g, function (_, inner) {
      // inner may itself contain diff spans; extract a plausible href from its text content.
      var textOnly = inner.replace(/<[^>]+>/g, "");
      var href = textOnly.trim();
      if (!/^https?:\/\//i.test(href)) {
        var m = /https?:\/\/\S+/i.exec(textOnly);
        href = m ? m[0] : "#";
      }
      return '<a class="mc-url" href="' + escapeAttr(href) + '" target="_blank" rel="noopener noreferrer">' + inner + "</a>";
    });
  }

  // ---------- Ratings ----------
  function loadRatings() {
    try { return JSON.parse(localStorage.getItem("gtnh_review_ratings_v1") || "{}") || {}; }
    catch (e) { return {}; }
  }
  function saveRatings() {
    try { localStorage.setItem(LS_KEY, JSON.stringify(ratings)); } catch (e) {}
  }
  function setRating(qid, patch) {
    var cur = ratings[qid] || {};
    for (var k in patch) cur[k] = patch[k];
    // Clean up empty records.
    if (!cur.rating && !(cur.note && cur.note.length)) delete ratings[qid];
    else ratings[qid] = cur;
    saveRatings();
  }
  function toggleRating(qid, val) {
    var cur = ratings[qid] || {};
    setRating(qid, { rating: cur.rating === val ? "" : val });
    updateRateButtonStates(qid);
    updateRatingCounter();
  }
  function updateRatingCounter() {
    var ok = 0, bad = 0, notes = 0;
    for (var k in ratings) {
      var r = ratings[k];
      if (r.rating === "ok") ok++;
      else if (r.rating === "bad") bad++;
      if (r.note && r.note.length) notes++;
    }
    ratingCounterEl.textContent = "👍 " + ok + "  👎 " + bad + "  ✏️ " + notes;
  }
  function exportRatings() {
    var payload = {
      exportedAt: new Date().toISOString(),
      count: Object.keys(ratings).length,
      ratings: ratings
    };
    var blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = "gtnh_review_ratings_" + new Date().toISOString().slice(0, 10) + ".json";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 0);
  }

  // ---------- UI binding ----------
  function bindUI() {
    $("prevBtn").onclick = $("prevBtn2").onclick = function () { go(-1); };
    $("nextBtn").onclick = $("nextBtn2").onclick = function () { go(1); };
    gotoInput.addEventListener("change", function () { gotoNum(parseInt(gotoInput.value, 10)); });

    $("renderToggle").addEventListener("change", function (e) {
      rendered = e.target.checked;
      render();
    });
    $("exportBtn").onclick = exportRatings;

    var filterEls = ["search", "filterCategory", "filterSeverity", "filterField", "filterRating", "filterHasOld"];
    filterEls.forEach(function (id) {
      var el = $(id);
      var ev = (id === "search") ? "input" : "change";
      el.addEventListener(ev, debounce(function () { applyFilters(false); }, id === "search" ? 200 : 0));
    });

    $("clearFilters").onclick = function () {
      $("search").value = "";
      $("filterCategory").value = "";
      $("filterSeverity").value = "";
      $("filterField").value = "";
      $("filterRating").value = "";
      $("filterHasOld").checked = false;
      applyFilters(false);
    };

    document.addEventListener("keydown", function (e) {
      var tag = (e.target && e.target.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
      if (e.key === "ArrowLeft") { go(-1); e.preventDefault(); }
      else if (e.key === "ArrowRight") { go(1); e.preventDefault(); }
    });
  }

  // ---------- Utils ----------
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }
  function escapeAttr(s) { return escapeHtml(s); }
  function cssEsc(s) { return String(s).replace(/["\\]/g, "\\$&"); }
  function debounce(fn, ms) {
    if (!ms) return fn;
    var t;
    return function () { clearTimeout(t); t = setTimeout(fn, ms); };
  }

  document.addEventListener("DOMContentLoaded", init);
})();
