---
layout: page
title: Home
id: home
permalink: /
---

<section>
  <p>I'm Choco_B, and this is my digital garden.</p>
</section>

<section style="margin-top: 4rem;">
  <h2>Latest</h2>
  <ul class="note-list">
    {% assign recent_notes = site.notes | sort: "last_modified_at" | reverse %}
    {% for note in recent_notes limit: 5 %}
      <li>
        <span class="note-date">{{ note.last_modified_at | date: "%B %d, %Y" }}</span>
        <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
      </li>
    {% endfor %}
  </ul>
</section>

<section style="margin-top: 4rem;">
  <h2>Writing</h2>
  <ul class="note-list">
    {% for note in recent_notes offset: 5 %}
      <li>
        <span class="note-date">{{ note.last_modified_at | date: "%B %d, %Y" }}</span>
        <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
      </li>
    {% endfor %}
  </ul>
</section>
