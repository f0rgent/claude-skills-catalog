// The f0rgent HUD scene: grid, scan line, radar sweep (top right), data bars (left), corner brackets.
export const SCENE = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice">
<style>
@keyframes scan{0%{transform:translateY(-120px)}100%{transform:translateY(1120px)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{0%,100%{opacity:.25}50%{opacity:1}}
@keyframes bar{0%,100%{transform:scaleX(.35)}50%{transform:scaleX(1)}}
@keyframes drift{to{transform:translateY(-40px)}}
.scan{animation:scan 9s linear infinite}
.sweep{transform-origin:150px 150px;animation:spin 6s linear infinite}
.p1{animation:pulse 2.4s ease-in-out infinite}
.p2{animation:pulse 3.1s ease-in-out infinite .8s}
.p3{animation:pulse 2.7s ease-in-out infinite 1.6s}
.b{transform-box:fill-box;transform-origin:left center;animation:bar 3s ease-in-out infinite}
.grid{animation:drift 12s linear infinite alternate}
@media (prefers-reduced-motion: reduce){*{animation:none!important}}
</style>
<defs>
<radialGradient id="glow" cx="50%" cy="40%" r="75%"><stop offset="0" stop-color="#0d2a2e"/><stop offset=".6" stop-color="#081417"/><stop offset="1" stop-color="#05090b"/></radialGradient>
<pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#2ee6c5" stroke-opacity=".07" stroke-width="1"/></pattern>
<pattern id="G" width="200" height="200" patternUnits="userSpaceOnUse"><path d="M200 0H0V200" fill="none" stroke="#2ee6c5" stroke-opacity=".12" stroke-width="1"/></pattern>
<linearGradient id="sl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2ee6c5" stop-opacity="0"/><stop offset=".85" stop-color="#2ee6c5" stop-opacity=".10"/><stop offset="1" stop-color="#2ee6c5" stop-opacity=".45"/></linearGradient>
<linearGradient id="sw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2ee6c5" stop-opacity="0"/><stop offset="1" stop-color="#2ee6c5" stop-opacity=".35"/></linearGradient>
</defs>
<rect width="1600" height="1000" fill="url(#glow)"/>
<g class="grid"><rect y="-40" width="1600" height="1080" fill="url(#g)"/><rect y="-40" width="1600" height="1080" fill="url(#G)"/></g>
<rect class="scan" x="0" y="0" width="1600" height="120" fill="url(#sl)"/>
<g fill="none" stroke="#2ee6c5" stroke-opacity=".55" stroke-width="2">
<path d="M24 84V24H84"/><path d="M1516 24H1576V84"/><path d="M24 916V976H84"/><path d="M1576 916V976H1516"/>
</g>
<svg x="0" y="0" width="1600" height="1000" viewBox="0 0 1600 1000" preserveAspectRatio="xMaxYMin meet">
<g transform="translate(1290 40)">
<g fill="none" stroke="#2ee6c5" stroke-opacity=".28"><circle cx="150" cy="150" r="130"/><circle cx="150" cy="150" r="88"/><circle cx="150" cy="150" r="44"/><path d="M150 20V280M20 150H280"/></g>
<path class="sweep" d="M150 150L280 150A130 130 0 0 0 242 58Z" fill="url(#sw)"/>
<circle class="p1" cx="208" cy="96" r="4" fill="#ff3d8b"/>
<circle class="p2" cx="104" cy="200" r="3" fill="#2ee6c5"/>
<circle class="p3" cx="190" cy="214" r="3" fill="#36c2ff"/>
<text x="20" y="306" fill="#2ee6c5" fill-opacity=".55" font-family="monospace" font-size="14" letter-spacing="3">SCAN // ACTIVE</text>
</g>
</svg>
<svg x="0" y="0" width="1600" height="1000" viewBox="0 0 1600 1000" preserveAspectRatio="xMinYMid meet">
<g transform="translate(48 330)" font-family="monospace" font-size="12" fill="#2ee6c5" fill-opacity=".5" letter-spacing="2">
<text y="0">AGENT.LOAD</text>
<rect class="b" y="10" width="150" height="6" fill="#2ee6c5" fill-opacity=".45" style="animation-delay:0s"/>
<text y="46">TOKENS/S</text>
<rect class="b" y="56" width="150" height="6" fill="#36c2ff" fill-opacity=".45" style="animation-delay:.7s"/>
<text y="92">CTX.WINDOW</text>
<rect class="b" y="102" width="150" height="6" fill="#2ee6c5" fill-opacity=".45" style="animation-delay:1.4s"/>
<text y="138">TOOLS</text>
<rect class="b" y="148" width="150" height="6" fill="#ff3d8b" fill-opacity=".45" style="animation-delay:2.1s"/>
</g>
</svg>
<text x="48" y="64" fill="#2ee6c5" fill-opacity=".45" font-family="monospace" font-size="14" letter-spacing="4">F0RGENT // HUD</text>
</svg>`
