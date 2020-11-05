# Kreativübung

**Aufgabe:** Erstelle deine eigene Zeichnung, die am Ende vorgestellt wird.

Hier nochmal der Überblick der zuvor genutzten Funktionen inkl. weiterer Möglichkeiten:

- `forward({Schritte nach vorne})` - Bewege die Schildkröte nach vorne
- `backward({Schritte nach zurück})` - Bewege die Schildkröte zurück
- `right({Winkel})` - Drehe die Schildkröte nach rechts
- `left({Winkel})` - Drehe die Schildkröte nach links
- `pencolor({Name der Farbe auf englisch})` - Ändere die Pinselfarbe
- `penup()` - Bewege die Schildkröte ohne einen Strich zu hinterlassen
- `pendown()` - Fange nach einem Aufruf von `penup()` wieder an zu zeichnen
- `circle({Radius},{gezeichneter Winkel})` - Zeichne einen Kreis
- `speed({Geschwindigkeit})` - Ändert die Zeichengeschwindigkeit der Schildkröte

Du kannst auch zwei Schildkröten erstellen, indem du sie in einer **Variable** zwischenspeicherst und von dort aus ansprichst.
Dies geht so:

```python
import turtle

# Es wird ein Object vom Typ Turtle erstellt und zwischengespeichert
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.forward(100)
turtle2.backward(100)
```