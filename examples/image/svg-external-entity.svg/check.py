import re

RISKS = [
    (r"<!ENTITY|<!DOCTYPE[^>]*\[", "declares entities (XXE)"),
    (r"<script\b", "contains <script>"),
    (r"\son[a-z]+\s*=", "has an on* event handler"),
    (r"(?:href|src)\s*=\s*[\"']?\s*javascript:", "links to javascript:"),
    (r"<foreignObject\b", "embeds HTML in foreignObject"),
    (r"(?:href|src)\s*=\s*[\"']?\s*https?://", "loads an external resource"),
]
with open("svg-external-entity.svg", encoding="utf-8") as f:
    svg = f.read()
found = [label for pattern, label in RISKS if re.search(pattern, svg, re.I)]
print("unsafe to serve inline: " + ", ".join(found) if found else "no active content found")
