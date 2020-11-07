# Aufgabe 2a - Das Schneckenhaus

Jetzt haben wir ein Rechteck und ein Dreick gezeichnet (Hausdach vom Nikolaus).
Im Folgenden wollen wir nun Viertelkreise zu einem Schneckenhaus formen.
Die Viertelkreise werden dabei immer größer.

Mit der Funktion `circle({Kreisradius},{gezeichneter Winkel})` lässt sich ein Kreisbogen erstellen.
Die Funktion wird in dieser Aufgabe mit den zwei Parametern verwendet.
Mit `circle(15, 90)` lässt sich bspw. ein Viertelkreis mit dem Radius von 15 Einheiten zeichnen.

Du kannst mit der Zählervariable auch rechnen, wie in der Schule. Hier ein paar Beispiele:

- Addition: `zaehler + 5`
- Subtraktion: `zaehler - 5`
- Multiplikation: `zaehler * 5`
- Division: `zaehler / 5` (Eine Division durch Null ist mathematisch nicht definiert und führt zu einem Programmfehler)
- Es gilt Punkt vor Strich; Klammern können helfen: `(zaehler + 1) * 5`

**Ziel:** Nutze das in der vorherigen Übung erlangte Wissen und die in dieser Übung vorgebene Funktion, um ein Schneckenhaus mit drei Umdrehungen zu zeichen.
Zuerst aber solltest Du mit der `circle` Funktion experimentieren und unterschiedlich große Kreise erstellen.
Denke auch daran, dass der Zähler bei `0` startet und schaue insbesondere auf das letzte Beispiel mit Punkt-vor-Strich, um dieses Problem zu lösen.

<details>
<summary>Lösung - Schneckenhaus</summary>

```python
import turtle

for zaehler in range(13):
  turtle.circle((zaehler + 1) * 15, 90)
```

</details>

# Aufgabe 2b - Buntes Schneckenhaus

Die Schildkröte kann auch die Pinselfarbe ändern. 
Hierzu wird die Funktion `pencolor({Name der Farbe})` verwendet.
Wird die Funktion ohne Parameter aufgerufen, gibt sie die aktuell eingestellte Farbe als Zeichenfolge aus:

```python
import turtle

# Setze die Pinselfarbe auf Purple
turtle.pencolor('purple')

# Gibt 'Purple' als Zeichenfolge aus
print(turtle.pencolor())
```

**Aufgabe**: Nutze die Farben `pink` und `blue` abwechselnd für jeden Viertelkreis des Schneckenhauses.

Für die Aufgabe benötigst Du folgende **Bedingungen**, um die Farbe zu wechseln:

- Ist die Farbe `blue` aktiv, so soll der nächste Viertelkreis `pink` gezeichnet werden.
- Ist die Farbe `pink` aktiv, so soll der nächste Viertelkreis `blue` gezeichnet werden.

Bedingungen werden mit dem Schlüsselwort `if` überprüft und beinhalten einen **Vergleichsoperator**.
Mit `else` lässt sich auf den Alternativfall überprüfen.

Für die Aufgabe lässt sich der Operator folgendermaßen verwenden:

```python
if turtle.pencolor() == 'blue':
    turtle.pencolor('pink')
else:
    # Alternativfall implementieren
```

<details>
<summary>Lösung - Buntes Schneckenhaus</summary>

```python
import turtle

turtle.pencolor('pink')

for zaehler in range(13):
  if turtle.pencolor() == 'pink':
    turtle.color('blue')
  else:
    turtle.color('pink')
  
  turtle.circle((zaehler + 1) * 15, 90)
```

</details>

# Aufgabe 2c - Buntes Schneckenhaus mit dem Modulo Operator

Natürlich kann man auch prüfen, ob der Zähler gerade oder ungerade ist.
In der Mathematik gibt es hierfür den **Modulo Operator** `%`.

Der Modulo Operator errechnet den Rest einer Division.
Beispiel: `5 % 2 = 1`

**Aufgabe:** Ändere die If-Bedingung so ab, dass Du folgende Bedingung nutzt:

```python
for zaehler in range(13):
  # Ersetze WERT_1 und WERT_2 durch die richtigen Ganzzahlen
  if zaehler % WERT_1 == WERT_2:
    # ...
  else:
    # ...
```

<details>
<summary>Lösung - Buntes Schneckenhaus (Modulo)</summary>

```python
import turtle

turtle.pencolor('pink')

for zaehler in range(13):
  if zaehler % 2 == 0:
    turtle.color('blue')
  else:
    turtle.color('pink')
  
  turtle.circle((zaehler + 1) * 15, 90)
```

</details>

---

Nun beherrscht Du schon For-Schleifen und If-Bedingungen.

[Hier](A3_Tannenbaum.md) gelangst Du zur nächsten Aufgabe.
