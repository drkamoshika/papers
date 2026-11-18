const overviewState={active:false,topic:"",data:null,error:""};
function readOverviewParams(params){overviewState.active=params.get("view")==="map";overviewState.topic=fieldDefinitions.some(f=>f.key===params.get("topic")&&f.key!=="classics")?params.get("topic"):"";}
function applyOverviewParams(url,paperId){url.searchParams.delete("view");url.searchParams.delete("topic");if(overviewState.active&&!paperId){for(const key of ["collection","field","source","q","sort"])url.searchParams.delete(key);url.searchParams.set("view","map");if(overviewState.topic)url.searchParams.set("topic",overviewState.topic);}}
function syncOverviewMode(){
 $("paper-browser").hidden=overviewState.active;$("overview").hidden=!overviewState.active;
 $("catalog-heading").textContent=overviewState.active?"全体マップ":"論文一覧";
 $("overview-tab").setAttribute("aria-pressed",String(overviewState.active));
 if(overviewState.active){for(const e of document.querySelectorAll("[data-collection]"))e.setAttribute("aria-pressed","false");renderOverview();}
}
function overviewPaperUrl(id){const p=overviewState.data.references[id],url=new URL(location.pathname,location.origin);url.searchParams.set("collection",p.collections.includes("foundations")?"foundations":"daily");url.searchParams.set("paper",id);return url;}
function overviewCitation(id,number){const p=overviewState.data.references[id];return '<a class="overview-citation" data-map-paper="'+esc(id)+'" href="'+esc(overviewPaperUrl(id).href)+'" title="'+esc(p.title)+'" aria-label="論文要約：'+esc(p.title)+'">['+esc(number)+']</a>';}
function overviewCites(refs,numbers){return '<div class="overview-cites">'+refs.map(id=>overviewCitation(id,numbers?numbers[id]:overviewState.data.references[id].title.split(":")[0])).join(" ")+'</div>';}
function overviewMethods(){return '<details class="overview-methods"><summary>このマップの収録範囲と読み方</summary><ul>'+overviewState.data.methodology.map(t=>'<li>'+esc(t)+'</li>').join("")+'</ul></details>';}
function overviewTopicButton(r){return '<button type="button" class="field-badge" data-field-key="'+r.key+'" data-map-topic="'+r.key+'" aria-pressed="'+(overviewState.topic===r.key)+'">'+esc(r.label)+'</button>';}
function renderOverview(){
 const root=$("overview");
 if(!overviewState.data){root.innerHTML='<p class="overview-empty">'+esc(overviewState.error||"全体マップを読み込み中...")+'</p>';return;}
 const data=overviewState.data,r=data.fields.find(f=>f.key===overviewState.topic),s=data.snapshot;
 const metadata='改稿 '+data.reviewDate+(data.corpusSnapshotDate?' · 対象文献 '+data.corpusSnapshotDate+'時点':'')+' · 論文公開日上限 '+s.latestPaperDate;
 if(!r){
  root.innerHTML='<p class="overview-intro">'+esc(data.scope)+'</p><p class="overview-meta">'+esc(metadata)+'<br>基礎 '+s.foundationCount+'件と新着 '+s.dailyCount+'件、計 '+s.uniqueCount+'件を母集団に、代表 '+s.referenceCount+'件を引用。</p>'+
  '<h2>7分野の到達点</h2><table class="overview-matrix"><thead><tr><th scope="col">分野</th><th scope="col">いまできること</th><th scope="col">残る境界</th></tr></thead><tbody>'+data.fields.map(f=>'<tr><td><a href="'+esc(overviewTopicUrl(f.key).href)+'" data-map-topic="'+f.key+'">'+esc(f.label)+' →</a><small>基礎文献 '+f.foundationCount+'件 · このレビューの引用 '+f.referenceIds.length+'件</small></td><td data-label="いまできること">'+esc(f.can)+'</td><td data-label="残る境界">'+esc(f.cannot)+'<div class="overview-row-cites">'+f.summaryRefs.map((id,i)=>overviewCitation(id,i+1)).join(" ")+'</div></td></tr>').join("")+'</tbody></table>'+
  '<h2>分野をまたいで見える変化</h2><div class="overview-themes">'+data.commonThemes.map(n=>'<section class="overview-theme"><h3>'+esc(n.title)+'</h3><p>'+esc(n.text)+'</p>'+overviewCites(n.refs)+'</section>').join("")+'</div>'+overviewMethods()+
  '<p class="overview-report-link"><a href="'+repo+'reports/overviews/README.md" target="_blank" rel="noopener noreferrer">GitHubで全体レビューを読む ↗</a></p>';
 }else{
  const numbers=Object.fromEntries(r.referenceIds.map((id,i)=>[id,i+1]));
  const otherRecent=r.additionalRecent||r.recent;
  const prose=n=>'<section class="overview-prose"><h3>'+esc(n.title)+'</h3><p>'+esc(n.text)+'</p>'+overviewCites(n.refs,numbers)+'</section>';
  const reading=r.reading.map(id=>{const p=data.references[id];return '<li><a href="'+esc(overviewPaperUrl(id).href)+'" data-map-paper="'+esc(id)+'">'+esc(p.title)+'</a><small>'+esc(p.date||"公開日未確認")+' · '+(p.collections.includes("foundations")?"基礎文献":"新着論文")+'</small></li>';}).join("");
  root.innerHTML='<button class="overview-back" type="button" data-map-topic="">← 7分野の一覧へ</button><nav class="overview-topic-nav" aria-label="全体マップの分野">'+data.fields.map(overviewTopicButton).join("")+'</nav><article class="overview-review">'+
  '<h2 class="overview-review-title" id="overview-review-title" tabindex="-1">'+esc(r.label)+'</h2><p class="overview-thesis">'+esc(r.thesis)+'</p><p class="overview-meta">'+esc(metadata)+'<br>収録基礎文献 '+r.foundationCount+'件 · このレビューの引用 '+r.referenceIds.length+'件（基礎 '+r.citedFoundationCount+'・新着 '+r.citedDailyCount+'）</p>'+
  '<div class="overview-takeaways"><div class="overview-takeaway"><strong>いまできること</strong><p>'+esc(r.can)+'</p></div><div class="overview-takeaway"><strong>残る境界</strong><p>'+esc(r.cannot)+'</p></div></div>'+overviewCites(r.summaryRefs,numbers)+
  '<nav class="overview-toc" aria-label="レビューの目次">'+overviewDeepToc(r)+'<a data-overview-section href="#overview-history">基礎からの積み上げ</a><a data-overview-section href="#overview-capabilities">現在の到達点</a>'+(otherRecent.length?'<a data-overview-section href="#overview-recent">関連する直近研究</a>':'')+'<a data-overview-section href="#overview-questions">次の課題</a><a data-overview-section href="#overview-connections">分野間の接点</a><a data-overview-section href="#overview-reading">読む順番</a></nav>'+
  overviewDeepContent(r,numbers)+
  '<section class="overview-review-section" id="overview-history"><h2>基礎からの積み上げ</h2>'+r.lineage.map(n=>'<div class="overview-stage">'+prose(n)+'</div>').join("")+'</section>'+
  '<section class="overview-review-section" id="overview-capabilities"><h2>現在の到達点と使える条件</h2>'+r.capabilities.map(n=>'<section class="overview-capability"><span class="overview-status">'+esc(n.status)+'</span><h3>'+esc(n.title)+'</h3><dl><dt>できていること</dt><dd>'+esc(n.can)+'</dd><dt>使える条件</dt><dd>'+esc(n.conditions)+'</dd><dt>残る境界</dt><dd>'+esc(n.boundary)+'</dd></dl>'+overviewCites(n.refs,numbers)+'</section>').join("")+'</section>'+
  (otherRecent.length?'<section class="overview-review-section" id="overview-recent"><h2>関連する直近研究</h2>'+otherRecent.map(prose).join("")+'</section>':'')+
  '<section class="overview-review-section" id="overview-questions"><h2>次の課題</h2><p class="overview-meta">以下は引用文献を踏まえた編者の整理です。</p>'+r.questions.map(prose).join("")+'</section>'+
  '<section class="overview-review-section" id="overview-connections"><h2>分野間の接点</h2><p class="overview-meta">技術的な接点を編者が整理しています。直接の引用関係を示すものではありません。</p><div class="overview-connections">'+r.connections.map(n=>'<section class="overview-connection"><button type="button" data-map-topic="'+n.topic+'">'+esc(data.fields.find(f=>f.key===n.topic).label)+' →</button><p>'+esc(n.text)+'</p>'+overviewCites(n.refs,numbers)+'</section>').join("")+'</div></section>'+
  '<section class="overview-review-section" id="overview-reading"><h2>読む順番</h2><ol class="overview-reading">'+reading+'</ol><p><a href="?collection=foundations&amp;field='+r.key+'" data-map-catalog="'+r.key+'">この分野の基礎文献 '+r.foundationCount+'件を一覧で見る →</a></p></section>'+
  '<details class="overview-references"><summary>引用文献 '+r.referenceIds.length+'件と出典</summary><ol>'+r.referenceIds.map(id=>{const p=data.references[id];return '<li><a href="'+esc(overviewPaperUrl(id).href)+'" data-map-paper="'+esc(id)+'">'+esc(p.title)+'</a><div class="overview-reference-meta">'+esc(p.date||"公開日未確認")+' · '+esc(p.id)+' · '+'登録時の確認範囲：'+esc(readLevel(p))+(p.rechecked?' · 今回の再確認 '+esc(p.rechecked)+'：'+esc(p.checkedScope):'')+(p.checkedNote?' · '+esc(p.checkedNote):'')+'</div><div class="overview-reference-links"><a href="'+esc(safeUrl(p.url))+'" target="_blank" rel="noopener noreferrer">原文 ↗</a>'+(p.checkedSource&&p.checkedSource!==p.url?'<a href="'+esc(safeUrl(p.checkedSource))+'" target="_blank" rel="noopener noreferrer">今回確認した一次資料 ↗</a>':'')+'</div></li>';}).join("")+'</ol></details>'+overviewMethods()+
  '<p class="overview-report-link"><a href="'+esc(repo+r.report)+'" target="_blank" rel="noopener noreferrer">このレビューをGitHubで読む ↗</a></p></article>';
 }
 for(const e of root.querySelectorAll("[data-overview-section]"))e.onclick=event=>{if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;event.preventDefault();document.getElementById(e.hash.slice(1))?.scrollIntoView({block:"start"});};
 for(const e of root.querySelectorAll("[data-map-topic]"))e.onclick=event=>{if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;event.preventDefault();openOverview(e.dataset.mapTopic);};
 for(const e of root.querySelectorAll("[data-map-paper]"))e.onclick=event=>{if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;const p=papers.find(p=>p.id===e.dataset.mapPaper);if(!p)return;event.preventDefault();openPaper(p);};
 for(const e of root.querySelectorAll("[data-map-catalog]"))e.onclick=event=>{if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;event.preventDefault();collectionFilter="foundations";fieldFilter=e.dataset.mapCatalog;sourceFilter="";$("search").value="";filtersChanged();window.scrollTo(0,0);};
}
function overviewTopicUrl(topic){const url=new URL(viewUrl());url.searchParams.set("view","map");url.searchParams.delete("paper");url.hash="";if(topic)url.searchParams.set("topic",topic);else url.searchParams.delete("topic");return url;}
function openOverview(topic=""){
 history.replaceState({...history.state,catalogScroll:window.scrollY,visibleLimit},"",viewUrl(selected));
 overviewState.active=true;overviewState.topic=topic;showCatalog();renderList();history.pushState({},"",overviewTopicUrl(topic));window.scrollTo(0,0);
 const title=$("overview-review-title");if(title)title.focus({preventScroll:true});
}
function initializeOverview(){
 $("overview-tab").onclick=()=>openOverview();
 fetch("./overview.json",{cache:"no-cache"}).then(r=>{if(!r.ok)throw Error(r.status);return r.json();}).then(data=>{
  if(!Array.isArray(data.fields)||data.fields.length!==7||!data.references)throw Error("invalid overview");overviewState.data=data;if(overviewState.active)renderOverview();
 }).catch(()=>{overviewState.error="全体マップを読み込めませんでした。ページを再読み込みしてください。論文一覧は各タブから利用できます。";if(overviewState.active)renderOverview();});
}


function overviewDeepToc(r){return r.deepDive?'<a data-overview-section href="#overview-technical">技術の中身</a><a data-overview-section href="#overview-comparison">手法の比較</a><a data-overview-section href="#overview-cases">実験を読み解く</a>':'';}
function overviewDeepContent(r,numbers){
 const d=r.deepDive;if(!d)return '';
 const chapters=d.chapters.map((h,i)=>'<section class="overview-deep-chapter" id="overview-chapter-'+i+'"><h3>'+esc(h.title)+'</h3>'+h.paragraphs.map(p=>'<div class="overview-deep-paragraph"><p>'+esc(p.text)+'</p>'+overviewCites(p.refs,numbers)+'</div>').join('')+'</section>').join('');
 const comparison='<table class="overview-comparison"><thead><tr><th scope="col">方法</th><th scope="col">何を変えるか</th><th scope="col">得られる利点</th><th scope="col">前提と交換条件</th></tr></thead><tbody>'+d.comparison.map(n=>'<tr><th scope="row">'+esc(n.name)+'</th><td data-label="何を変えるか">'+esc(n.mechanism)+'</td><td data-label="得られる利点">'+esc(n.strength)+'</td><td data-label="前提と交換条件">'+esc(n.boundary)+overviewCites(n.refs,numbers)+'</td></tr>').join('')+'</tbody></table>';
 const cases=d.cases.map(n=>'<section class="overview-case-analysis"><h3>'+esc(n.title)+'</h3>'+[['question','研究の問い'],['design','設計と対照'],['result','論文が報告する結果'],['meaning','位置づけ・編者の解釈'],['boundary','結論の範囲']].map(([key,label])=>'<div class="overview-case-part '+(key==='result'?'overview-case-result':'')+'"><h4>'+esc(label)+'</h4><p>'+esc(n[key])+'</p></div>').join('')+overviewCites(n.refs,numbers)+'</section>').join('');
 return '<section class="overview-review-section" id="overview-technical"><h2>技術の中身と論文同士の関係</h2><ol class="overview-subtoc">'+d.chapters.map((h,i)=>'<li><a data-overview-section href="#overview-chapter-'+i+'">'+esc(h.title)+'</a></li>').join('')+'</ol>'+chapters+'</section><section class="overview-review-section" id="overview-comparison"><h2>手法を比較する</h2>'+comparison+'</section><section class="overview-review-section" id="overview-cases"><h2>具体的研究を読み解く</h2>'+cases+'</section>';
}
