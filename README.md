# csp-status

tl;dr: Looking into how many top websites have actually adopted CSP.



List of CSP directives and their usage in alexa top 10,000 sites:

[('prefetch-src', 0), ('manifest-src', 2), ('referrer', 2), ('sandbox', 5), ('worker-src', 14), ('form-action', 23), ('block-all-mixed-content', 41), ('object-src', 76), ('media-src', 101), ('upgrade-insecure-requests', 102), ('font-src', 103), ('style-src', 111), ('img-src', 126), ('connect-src', 130), ('frame-ancestors', 147), ('script-src', 153), ('frame-src', 158), ('default-src', 183)]




1) 90% of implementation are bypassable anyway.[1] 

2) In Alexa top 1000, about 95(i.e. >1%) have CSP implemented. 
(If you look at alexa top 10,000, the number goes down to about 450 (>0.5%) have implemented CSP in some way.)

So, actual beneficiaries of CSP - 10% of the 95 sites in alexa top 1000. Thats a handful of sites.

Just looking at implementation, makes me think, was making CSP a standard wise idea?










[1]https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45542.pdf
