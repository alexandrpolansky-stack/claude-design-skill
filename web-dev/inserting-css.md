# Vkládání CSS

Tři způsoby, jak dostat CSS do dokumentu.

Související: [HTML a CSS](html-a-css.md) · [Stylizace textu](stylizace-textu.md)

---
title: Inserting CSS
updated: 2023-07-21 14:43:58Z
created: 2023-07-21 14:00:10Z
latitude: 50.07553810
longitude: 14.43780050
altitude: 0.0000
---

Css může být psáno do HTML dokumentu nebo může být vytvořen CSS dokument, který linkneme

<link href=“css/style.css” type=“text/css” rel=“stylesheet” />

Můžeme taky psát CSS do dokumentu, což vypadá takhle

<style type=“text/css”>
            h1 {
                color: green;
            }

A nebo takhle

<h1 style="color: blue;">This will be a blue heading</h1>