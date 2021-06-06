//Import JS from other docs. Not proofed.


let theOtherScript = 'http://example.com/js/script.js';

let el = document.createElement('script');
el.async = false;
el.src = theOtherScript;
el.type = 'text/javascript';

(document.getElementsByTagName('HEAD')[0]||document.body)
