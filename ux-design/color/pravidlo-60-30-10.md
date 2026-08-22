# Pravidlo 60-30-10

Poměr neutrální, primární a akcentní barvy v paletě.

Související: [Teorie barev](color-theory.md) · [Kontrast a barva](../pravidla/kontrast-a-barva.md) · [Anti-slop](../pravidla/anti-slop.md)

> **OVERRIDE.** Tahle nota je ve vrstvě 3 (import) a jedno její doporučení vyrábí porušení WCAG.
>
> **Neplatí:** „barva by měla mít tak 90% saturace, 90% brightness" (níže v textu). Barva s jasem
> kolem 90 % je skoro vždycky moc světlá na to, aby na ní bílý text splnil 4,5:1, a často i na to,
> aby proti bílému pozadí splnila 3:1 podle WCAG 1.4.11. Akcent přitom typicky nese primární CTA,
> tedy nejdůležitější prvek stránky.
>
> **Co dělat místo toho:** drž akcent ve dvou variantách.
>
> | Varianta | K čemu | Podmínka |
> |---|---|---|
> | Tmavší | plocha pod bílým textem (CTA tlačítko, badge) | text na ní minimálně 4,5:1 |
> | Jasná | rámeček, ikona, podtržení, drobný detail | proti pozadí minimálně 3:1 (WCAG 1.4.11) |
>
> Sytost si nech, ubírej jas. „Pop" dělá kontrast vůči zbytku palety, ne absolutní jas. Měř to
> nástrojem, neodhaduj. Autoritativní zdroj:
> [Kontrast a barva](../pravidla/kontrast-a-barva.md), třída A.
>
> **Samotný poměr 60-30-10** je kompoziční heuristika bez měření, třída C. Výchozí rozdělení plochy,
> ne pravidlo.
>
> Zbytek noty je přepis z kurzu, včetně rady generovat paletu v ChatGPT a odstavce, který je sám
> odpovědí z ChatGPT. Je tu jako záznam, ne jako opora.

Hodně často používáno v interier designu, ale také funguje dost dobře v UI
![Pasted image 20231204214019](../_assets/pasted-image-20231204214019.png)
60% = **je naše neutrální barva** nebo base color = většinou neutrální, creamy, white, dark
30% = **primární barva** to může být brand color - **Red Jest Grey Color**
10% = **Call to action** color = barva **look at me, click at me etc.**

Nejbezpečnější cesta je jít s barvami jako v prvním příkladu. 60% bílá, 30% text černá, 10% call to action barva

Chat GPT dokáže vygenerovat 60-30-10 barvy, ale poslední barva musí mít **POP;WOW efekt** - pokud to bude **mrtvá modrá**(Tahle), tak to nebude fungovat. Fungují dobře barvy co mají **vysokou saturaci** a jsou útočné (sytě modrá, lime green, sytě žlutá etc.); barva by měla mít tak **90% saturace, 90% brightness** a **vyvarovat** se hue **H40-H120**

**Příklady**

What is 60 30 10 rule in web design

 The 60-30-10 rule in web design refers to a guideline for creating a visually appealing and balanced color scheme. The rule suggests using a dominant color for 60% of the design, a secondary color for 30%, and an accent color for the remaining 10%. This helps to create a cohesive look that is both aesthetically pleasing and easy on the eyes.