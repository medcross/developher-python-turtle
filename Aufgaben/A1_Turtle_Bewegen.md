# Aufgabe 1a - Text ausgeben

**Ziel:** Es wird `Hallo Welt` angezeigt.

Ein Einstieg in die Programmierung wäre nicht richtig, ohne der Welt `Hallo` zu sagen.

In Python kannst du eine Ausgabe mit der Anweisung `print()` machen.
Es handelt sich hierbei um einen **Funktionsaufruf**.

In den Klammern `()` der Funktion übergibst Du einen **Parameter**.
In diesem Fall `'Hallo Welt'`.
Die Anführungszeichen `''` kenzeichnen eine **Zeichenfolge**, die Du direkt in die Funktion `print` übergiebst.

Wir erhalten also `print('Hallo Welt')`.

**Zusammenfassung:**

- `print()` ist eine Funktion zur Ausgabe von Werten; auch Zahlen
- Eine Funktion kann eine bestimmte Anzahl oder keine Parameter entgegenehmen

**Info:** Richtig eingesetzt sind Ausgaben nützliche Hilfsmittel, um das Verhalten deines Programmes besser zu verstehen.

---

# Aufgabe 1b - Bewege die Schildkröte

**Ziel**: Die Schildkröte erscheint in der Mitte des Feldes und bewegt sich in verschiedene Richtungen.

Programmierer erfinden das Rad nicht immer neu.
So hat für uns auch schon jemand den "Pinsel" und die Leinwand erfunden.
Natürlich haben die dafür verantwortlichen Personen diese mit Quellcode umgesetzt.
Die Gesamtheit des Quellcodes wird in Python in einem **Modul** gebündelt.

**Info:** Mittels Modulen können alltägliche Probleme vieler Programmierer mit anderen Programmieren geteilt werden, die ihr Programm darau aufbauen.
Es wäre doch lästig und ineffizient, wenn man immer wieder von Null anfangen muss.
Aus diesem Grund bietet auch die Programmiersprache selber die wichtigsten Abstraktionen in Form einer Standardbibliothek an.

Wir nutzen heute ausschließlich das `turtle` Modul. Dies müssen wir aber zunächst importieren, damit der Python Interpreter weiß, wass wir benötigen.

Hierfür schreiben wir ganz oben in den Quelltext `import turtle`

Um auf Funktionen des Moduls zugreifen zu können, nutzt man die Syntax `turtle.{Name der Funktion}`

Funktionen zum Bewegen der Schildkröte sind bspw.

- `forward(100)`: Gehe 100 Scrhitte in Kopfrichtung nach vorne
- `backward(100)`: Gehe 100 Schritte rückwärts
- `left(90)`: Drehe 90° nach links
- `right(90)`: Drehe 90° nach rechts

Schaffst Du es, die Schildkröte zu navigieren?

# Aufgabe 1c - Zeichne ein Quadrat

**Ziel:** Zeichne ein Quadrat mit gleichen Seitenlängen durch Bewegen und Drehen der Schildkröte.
Dabei solltest du am Ende wieder beim Startpunkt ankommen.

<details>
<summary>Lösung - Quadrat</summary>

```python
import turtle

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
```

</details>

**Wichtig: Speichere den Quelltext zum Zeichen des Rechtecks auf deinem Computer, um ihn später wiederzuverwenden**

# Aufgabe 1d - Das Haus vom Nikolaus

**Ziel:** Kannst Du auch das Haus vom Nikolaus zeichnen, ohne dabei eine Linie zweimal zu zeichnen?

Gebe zusätzlich beim Zeichnen der Linien folgendes aus:

```
Das
ist
das
Haus
vom
Ni-
ko-
laus!
```

<details>
<summary>Lösung - Haus vom Nikolaus</summary>

```python
import turtle

print('Das')
turtle.left(45)
turtle.forward(142)

print('ist')
turtle.left(135)
turtle.forward(100)

print('das')
turtle.left(135)
turtle.forward(142)

print('Haus')
turtle.right(135)
turtle.forward(100)

print('vom')
turtle.right(90)
turtle.forward(100)

print('Ni-')
turtle.right(45)
turtle.forward(71)

print('Ko-')
turtle.right(90)
turtle.forward(71)

print('Laus-')
turtle.right(45)
turtle.forward(100)
```

</details>

# Aufgabe 1e - Wir bauen eine Siedlung mit For-Schleifen

Wie geht der Spruch weiter? `Das ist das Haus vom Nikolaus ... und nebenan vom Weihnachtsmann`

**Ziel:** Baue mehrere der Häuser aus Aufgabe nebeneinander. Setze dafür eine Schleife ein, um den gleichen Code nicht unnötig oft kopieren zu müssen.

Um in der Programmierung die gleichen Anweisungen zu wiederholen, nutzt man **Schleifen**.
Eine Form der Schleife ist die Zählschleife. Man definiert eine **Variable**, welche den Zähler speichert und bei jedem Durchlauf erhöht (inkrementiert).

In Python nutzt man dazu das Schlüsselwort (die Vokabel) `for`. Daher wird die Schleife auch als **For-Schleife** bezeichnet.

Hier ein Beispiel einer solchen For-Schleife, die nach oben zählt und den Wert des Zählers anzeigt:

```python
for zaehler in range(5):
    print(zaheler)
```

`range(5)` ist wieder eine Funktion. Der Parameter `5` erzeugt eine Sequenz von Zahlen von 0 bis 4.

Die Ausgabe eines solchen Programms ist folgende:

```
0
1
2
3
4
```

**Denkaufgabe:** Fällt Dir etwas auf? Besonders wo der Zähler startet und endet?

Ersetze nun das Print durch den Code für das Nikolaushaus.
Achte besonders auf die einfache Einrückung, die du mit der Tabulatortaste erreichst.
Sie ist wichtig, um dem Python Interpreter zu zeigen, welche Anweisungen zur Schleife gehören.
Der Doppelpunkt `:` zu Beginn der SChleifenanweisung wird ebenfalls als Signalisierung des Beginns vom Schleifenkörper benötigt.

Schreibe vor die Schleife noch folgenden Code, um die Schildkröte schneller zu machen.

```python
import turtle

turtle.speed(10)

# Code für die for-Schleife soll hier hin kommen
```

**Tipp:** Du musst am Ende des Schleifenkörpers die Schildkröte ein Stück nach rechts drehen, um mehr Platz zu haben.

<details>
<summary>Lösung - Haus vom Nikolaus mit Zählerschleife</summary>

```python
import turtle

turtle.speed(10)

for zaehler in range(5)
    print('Das')
    turtle.left(45)
    turtle.forward(142)

    print('ist')
    turtle.left(135)
    turtle.forward(100)

    print('das')
    turtle.left(135)
    turtle.forward(142)

    print('Haus')
    turtle.right(135)
    turtle.forward(100)

    print('vom')
    turtle.right(90)
    turtle.forward(100)

    print('Ni-')
    turtle.right(45)
    turtle.forward(71)

    print('Ko-')
    turtle.right(90)
    turtle.forward(71)

    print('Laus-')
    turtle.right(45)
    turtle.forward(100)
```

</details>

---

[Hier](A2_Schneckenhaus.md) gelangst du zur Aufgabe 2