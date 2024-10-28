---
title: 
aliases: 
tags: 
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
update: <% tp.file.last_modified_date("YYYY/MM/DD HH:mm:ss") %>
feeling: 
summary: 
draft: true
---
# Missions ✨


# Thoughts 💬


# Notes 📝

```dataview
TABLE impact as Impact, created as Created
FROM -"6. Vault"
WHERE dateformat(file.ctime,"yyyy-MM-dd") = dateformat(date(this.created, "yyyy-MM-dd HH:mm:ss"), "yyyy-MM-dd")
SORT rank DESC, created DESC
```