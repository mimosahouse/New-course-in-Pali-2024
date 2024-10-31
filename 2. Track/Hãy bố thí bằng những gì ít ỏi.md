---
aliases: 
created: 2024-10-31 06:10:89
tags: 
feeling: 
summary:
---
Hãy bố thí bằng những gì ít ỏi

---
Một ngày cuối cùng của tháng 10. Nay đi làm với Paul, hơi đau lưng, nhưng không bị căng thẳng quá.
Nay có 2 anh bộ đội đến nhà Paul nữa, chửng biết có chuyện gì.
---
---





# Missions ✨


# Thoughts 💬


# Notes

```dataview
TABLE impact as Impact, created as Created
FROM -"6. Vault"
WHERE dateformat(file.ctime,"yyyy-MM-dd") = dateformat(date(this.created, "yyyy-MM-dd HH:mm:ss"), "yyyy-MM-dd")
SORT rank DESC, created DESC
```