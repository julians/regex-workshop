# Kleiner RegEx-Workshop

## Suchen und Ersetzen im Editor:

**Textmate: ⌘+F** – im Fenster »Regular Expression« checken.

**Sublime Text: ⌘+⌥+F** – den Regular-Expression-Button unten links anklicken.



http://regexpal.com


```python
import re

pattern = re.compile(r";")
pattern.findall("hallo;zwei;drei")
>>>[';', ';']

re.match(r";", "hallo;zwei;drei")
>>>
re.search(r";", "hallo;zwei;drei").group(0)
>>>';'
re.split(r";", "hallo;zwei;drei")
>>>['hallo', 'zwei', 'drei']
```