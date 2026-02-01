/*
1. Open item page
2. Let page load
3. Open bookmarklet
4. Copy filename from prompt
5. PDF print PDF in the import folder
*/
javascript: (function () {
    function rc(sel) {f = document.querySelectorAll(sel).forEach((el) => {el.remove();})};
    [
        'div[slot="recommendations"]',
        'div[slot="suggestions"]',
        'div[slot="advertising"]',
        'div[slot="header"]',
        'div[slot="footer"]',
        'finn-contact-button',
    ].forEach((e) => { rc(e); });

document.body.prepend(document.querySelector("podium-layout").shadowRoot.querySelector("h1"));
document.querySelector("podium-layout").shadowRoot.querySelectorAll("button").forEach((el) => {el.remove();});
document.querySelector("podium-layout").shadowRoot.querySelectorAll("img[alt='Galleribilde']").forEach((e)=>{
    div=document.createElement("div");
    div.style.breakInside="avoid";
    div.style.pageBreakInside="avoid";
    var img = document.createElement('img');
    if (e.dataset.src) { img.src = e.dataset.src; } else { img.src = e.src;};
    img.style.maxWidth="100%";
    img.style.breakInside="avoid";
    img.style.pageBreakInside="avoid";
    div.appendChild(img);
    document.querySelector("body").appendChild(div);
    document.querySelector("body").appendChild(document.createElement("br"));
});
document.querySelectorAll('*').forEach(function(e){
    e.style.fontFamily = "sans-serif";
    e.style.lineHeight = "1";
});
setTimeout(function() { 
    prompt("Save PDF as",document.location.href.match(/\d{7,}/)[0]);
    window.print();
    }, 2000);
})()