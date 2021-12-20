!function(N){N.fn.extend({slimScroll:function(T){var A=N.extend({width:"auto",height:"250px",size:"7px",color:"#000",position:"right",distance:"1px",start:"top",opacity:.4,alwaysVisible:!1,disableFadeOut:!1,railVisible:!1,railColor:"#333",railOpacity:.2,railDraggable:!0,railClass:"slimScrollRail",barClass:"slimScrollBar",wrapperClass:"slimScrollDiv",allowPageScroll:!1,wheelStep:20,touchScrollStep:200,borderRadius:"0",railBorderRadius:"0"},T);return this.each(function(){var n,e,a,i,o,s,r,l,c="<div></div>",u=30,d=!1,p=N(this);if(p.parent().hasClass(A.wrapperClass)){var f=p.scrollTop();if(b=p.closest("."+A.barClass),g=p.closest("."+A.railClass),C(),N.isPlainObject(T)){if("height"in T&&"auto"==T.height){p.parent().css("height","auto"),p.css("height","auto");var h=p.parent().parent().height();p.parent().css("height",h),p.css("height",h)}if("scrollTo"in T)f=parseInt(A.scrollTo);else if("scrollBy"in T)f+=parseInt(A.scrollBy);else if("destroy"in T)return b.remove(),g.remove(),void p.unwrap();E(f,!1,!0)}}else if(!(N.isPlainObject(T)&&"destroy"in T)){A.height="auto"==A.height?p.parent().height():A.height;var m=N(c).addClass(A.wrapperClass).css({position:"relative",overflow:"hidden",width:A.width,height:A.height});p.css({overflow:"hidden",width:A.width,height:A.height});var v,g=N(c).addClass(A.railClass).css({width:A.size,height:"100%",position:"absolute",top:0,display:A.alwaysVisible&&A.railVisible?"block":"none","border-radius":A.railBorderRadius,background:A.railColor,opacity:A.railOpacity,zIndex:90}),b=N(c).addClass(A.barClass).css({background:A.color,width:A.size,position:"absolute",top:0,opacity:A.opacity,display:A.alwaysVisible?"block":"none","border-radius":A.borderRadius,BorderRadius:A.borderRadius,MozBorderRadius:A.borderRadius,WebkitBorderRadius:A.borderRadius,zIndex:99}),w="right"==A.position?{right:A.distance}:{left:A.distance};g.css(w),b.css(w),p.wrap(m),p.parent().append(b),p.parent().append(g),A.railDraggable&&b.bind("mousedown",function(e){var i=N(document);return a=!0,t=parseFloat(b.css("top")),pageY=e.pageY,i.bind("mousemove.slimscroll",function(e){currTop=t+e.pageY-pageY,b.css("top",currTop),E(0,b.position().top,!1)}),i.bind("mouseup.slimscroll",function(t){a=!1,L(),i.unbind(".slimscroll")}),!1}).bind("selectstart.slimscroll",function(t){return t.stopPropagation(),t.preventDefault(),!1}),g.hover(function(){x()},function(){L()}),b.hover(function(){e=!0},function(){e=!1}),p.hover(function(){n=!0,x(),L()},function(){n=!1,L()}),p.bind("touchstart",function(t,e){t.originalEvent.touches.length&&(o=t.originalEvent.touches[0].pageY)}),p.bind("touchmove",function(t){(d||t.originalEvent.preventDefault(),t.originalEvent.touches.length)&&(E((o-t.originalEvent.touches[0].pageY)/A.touchScrollStep,!0),o=t.originalEvent.touches[0].pageY)}),C(),"bottom"===A.start?(b.css({top:p.outerHeight()-b.outerHeight()}),E(0,!0)):"top"!==A.start&&(E(N(A.start).position().top,null,!0),A.alwaysVisible||b.hide()),v=this,window.addEventListener?(v.addEventListener("DOMMouseScroll",y,!1),v.addEventListener("mousewheel",y,!1)):document.attachEvent("onmousewheel",y)}function y(t){if(n){var e=0;(t=t||window.event).wheelDelta&&(e=-t.wheelDelta/120),t.detail&&(e=t.detail/3);var i=t.target||t.srcTarget||t.srcElement;N(i).closest("."+A.wrapperClass).is(p.parent())&&E(e,!0),t.preventDefault&&!d&&t.preventDefault(),d||(t.returnValue=!1)}}function E(t,e,i){d=!1;var n=t,a=p.outerHeight()-b.outerHeight();if(e&&(n=parseInt(b.css("top"))+t*parseInt(A.wheelStep)/100*b.outerHeight(),n=Math.min(Math.max(n,0),a),n=0<t?Math.ceil(n):Math.floor(n),b.css({top:n+"px"})),n=(r=parseInt(b.css("top"))/(p.outerHeight()-b.outerHeight()))*(p[0].scrollHeight-p.outerHeight()),i){var o=(n=t)/p[0].scrollHeight*p.outerHeight();o=Math.min(Math.max(o,0),a),b.css({top:o+"px"})}p.scrollTop(n),p.trigger("slimscrolling",~~n),x(),L()}function C(){s=Math.max(p.outerHeight()/p[0].scrollHeight*p.outerHeight(),u),b.css({height:s+"px"});var t=s==p.outerHeight()?"none":"block";b.css({display:t})}function x(){if(C(),clearTimeout(i),r==~~r){if(d=A.allowPageScroll,l!=r){var t=0==~~r?"top":"bottom";p.trigger("slimscroll",t)}}else d=!1;l=r,s>=p.outerHeight()?d=!0:(b.stop(!0,!0).fadeIn("fast"),A.railVisible&&g.stop(!0,!0).fadeIn("fast"))}function L(){A.alwaysVisible||(i=setTimeout(function(){A.disableFadeOut&&n||e||a||(b.fadeOut("slow"),g.fadeOut("slow"))},1e3))}}),this}}),N.fn.extend({slimscroll:N.fn.slimScroll})}(jQuery),function(t,e){"use strict";"function"==typeof define&&define.amd?define([],function(){return e.apply(t)}):"object"==typeof exports?module.exports=e.call(t):t.Waves=e.call(t)}("object"==typeof global?global:this,function(){"use strict";var e=e||{},n=document.querySelectorAll.bind(document),s=Object.prototype.toString,r="ontouchstart"in window;function a(t){var e=typeof t;return"function"===e||"object"===e&&!!t}function u(t){var e,i=s.call(t);return"[object String]"===i?n(t):a(t)&&/^\[object (Array|HTMLCollection|NodeList|Object)\]$/.test(i)&&t.hasOwnProperty("length")?t:a(e=t)&&0<e.nodeType?[t]:[]}function d(t){var e,i,n,a,o={top:0,left:0},s=t&&t.ownerDocument;return e=s.documentElement,void 0!==t.getBoundingClientRect&&(o=t.getBoundingClientRect()),i=null!==(a=n=s)&&a===a.window?n:9===n.nodeType&&n.defaultView,{top:o.top+i.pageYOffset-e.clientTop,left:o.left+i.pageXOffset-e.clientLeft}}function p(t){var e="";for(var i in t)t.hasOwnProperty(i)&&(e+=i+":"+t[i]+";");return e}var f={duration:750,delay:200,show:function(t,e,i){if(2===t.button)return!1;e=e||this;var n=document.createElement("div");n.className="waves-ripple waves-rippling",e.appendChild(n);var a=d(e),o=0,s=0;s=0<=(s="touches"in t&&t.touches.length?(o=t.touches[0].pageY-a.top,t.touches[0].pageX-a.left):(o=t.pageY-a.top,t.pageX-a.left))?s:0,o=0<=o?o:0;var r="scale("+e.clientWidth/100*3+")",l="translate(0,0)";i&&(l="translate("+i.x+"px, "+i.y+"px)"),n.setAttribute("data-hold",Date.now()),n.setAttribute("data-x",s),n.setAttribute("data-y",o),n.setAttribute("data-scale",r),n.setAttribute("data-translate",l);var c={top:o+"px",left:s+"px"};n.classList.add("waves-notransition"),n.setAttribute("style",p(c)),n.classList.remove("waves-notransition"),c["-webkit-transform"]=r+" "+l,c["-moz-transform"]=r+" "+l,c["-ms-transform"]=r+" "+l,c["-o-transform"]=r+" "+l,c.transform=r+" "+l,c.opacity="1";var u="mousemove"===t.type?2500:f.duration;c["-webkit-transition-duration"]=u+"ms",c["-moz-transition-duration"]=u+"ms",c["-o-transition-duration"]=u+"ms",c["transition-duration"]=u+"ms",n.setAttribute("style",p(c))},hide:function(t,e){for(var i=(e=e||this).getElementsByClassName("waves-rippling"),n=0,a=i.length;n<a;n++)o(t,e,i[n])}},l={input:function(t){var e=t.parentNode;if("i"!==e.tagName.toLowerCase()||!e.classList.contains("waves-effect")){var i=document.createElement("i");i.className=t.className+" waves-input-wrapper",t.className="waves-button-input",e.replaceChild(i,t),i.appendChild(t);var n=window.getComputedStyle(t,null),a=n.color,o=n.backgroundColor;i.setAttribute("style","color:"+a+";background:"+o),t.setAttribute("style","background-color:rgba(0,0,0,0);")}},img:function(t){var e=t.parentNode;if("i"!==e.tagName.toLowerCase()||!e.classList.contains("waves-effect")){var i=document.createElement("i");e.replaceChild(i,t),i.appendChild(t)}}};function o(t,e,i){if(i){i.classList.remove("waves-rippling");var n=i.getAttribute("data-x"),a=i.getAttribute("data-y"),o=i.getAttribute("data-scale"),s=i.getAttribute("data-translate"),r=350-(Date.now()-Number(i.getAttribute("data-hold")));r<0&&(r=0),"mousemove"===t.type&&(r=150);var l="mousemove"===t.type?2500:f.duration;setTimeout(function(){var t={top:a+"px",left:n+"px",opacity:"0","-webkit-transition-duration":l+"ms","-moz-transition-duration":l+"ms","-o-transition-duration":l+"ms","transition-duration":l+"ms","-webkit-transform":o+" "+s,"-moz-transform":o+" "+s,"-ms-transform":o+" "+s,"-o-transform":o+" "+s,transform:o+" "+s};i.setAttribute("style",p(t)),setTimeout(function(){try{e.removeChild(i)}catch(t){return!1}},l)},r)}}var c={touches:0,allowEvent:function(t){var e=!0;return/^(mousedown|mousemove)$/.test(t.type)&&c.touches&&(e=!1),e},registerEvent:function(t){var e=t.type;"touchstart"===e?c.touches+=1:/^(touchend|touchcancel)$/.test(e)&&setTimeout(function(){c.touches&&(c.touches-=1)},500)}};function i(e){var i=function(t){if(!1===c.allowEvent(t))return null;for(var e=null,i=t.target||t.srcElement;null!==i.parentElement;){if(i.classList.contains("waves-effect")&&!(i instanceof SVGElement)){e=i;break}i=i.parentElement}return e}(e);if(null!==i){if(i.disabled||i.getAttribute("disabled")||i.classList.contains("disabled"))return;if(c.registerEvent(e),"touchstart"===e.type&&f.delay){var n=!1,a=setTimeout(function(){a=null,f.show(e,i)},f.delay),o=function(t){a&&(clearTimeout(a),a=null,f.show(e,i)),n||(n=!0,f.hide(t,i))};i.addEventListener("touchmove",function(t){a&&(clearTimeout(a),a=null),o(t)},!1),i.addEventListener("touchend",o,!1),i.addEventListener("touchcancel",o,!1)}else f.show(e,i),r&&(i.addEventListener("touchend",f.hide,!1),i.addEventListener("touchcancel",f.hide,!1)),i.addEventListener("mouseup",f.hide,!1),i.addEventListener("mouseleave",f.hide,!1)}}return e.init=function(t){var e=document.body;"duration"in(t=t||{})&&(f.duration=t.duration),"delay"in t&&(f.delay=t.delay),r&&(e.addEventListener("touchstart",i,!1),e.addEventListener("touchcancel",c.registerEvent,!1),e.addEventListener("touchend",c.registerEvent,!1)),e.addEventListener("mousedown",i,!1)},e.attach=function(t,e){var i,n;t=u(t),"[object Array]"===s.call(e)&&(e=e.join(" ")),e=e?" "+e:"";for(var a=0,o=t.length;a<o;a++)n=(i=t[a]).tagName.toLowerCase(),-1!==["input","img"].indexOf(n)&&(l[n](i),i=i.parentElement),-1===i.className.indexOf("waves-effect")&&(i.className+=" waves-effect"+e)},e.ripple=function(t,e){var i=(t=u(t)).length;if((e=e||{}).wait=e.wait||0,e.position=e.position||null,i)for(var n,a,o,s={},r=0,l={type:"mousedown",button:1},c=function(t,e){return function(){f.hide(t,e)}};r<i;r++)if(n=t[r],a=e.position||{x:n.clientWidth/2,y:n.clientHeight/2},o=d(n),s.x=o.left+a.x,s.y=o.top+a.y,l.pageX=s.x,l.pageY=s.y,f.show(l,n),0<=e.wait&&null!==e.wait){setTimeout(c({type:"mouseup",button:1},n),e.wait)}},e.calm=function(t){for(var e={type:"mouseup",button:1},i=0,n=(t=u(t)).length;i<n;i++)f.hide(e,t[i])},e.displayEffect=function(t){console.error("Waves.displayEffect() has been deprecated and will be removed in future version. Please use Waves.init() to initialize Waves effect"),e.init(t)},e}),function(t){"use strict";function i(t){return new RegExp("(^|\\s+)"+t+"(\\s+|$)")}var n,a,o;function e(t,e){(n(t,e)?o:a)(t,e)}o="classList"in document.documentElement?(n=function(t,e){return t.classList.contains(e)},a=function(t,e){t.classList.add(e)},function(t,e){t.classList.remove(e)}):(n=function(t,e){return i(e).test(t.className)},a=function(t,e){n(t,e)||(t.className=t.className+" "+e)},function(t,e){t.className=t.className.replace(i(e)," ")});var s={hasClass:n,addClass:a,removeClass:o,toggleClass:e,has:n,add:a,remove:o,toggle:e};"function"==typeof define&&define.amd?define(s):t.classie=s}(window);