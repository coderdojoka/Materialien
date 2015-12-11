Um die Markdown-Dokumente über unsere CoderDojo-Latex Vorlage in PDFs zu übersetzen, wird pandoc verwendet.

Dafür muss natürlich [pandoc](http://pandoc.org) und Latex installiert sein.

Zum Kompilieren von Code in Latex wird des Python-Modul _pygements_ (`pip install pygments`) benötigt.
Außerdem wird das Python-Modul _pandocfilters_ benötigt, um den Code aus den Markdown-Dateien korrekt zu extrahieren und mithilfe von _pygments_ darzustellen.

Um nun ein Markdown-Dokument zu einem PDF zu konvertieren gibt es das Skript **to_latex.sh**, dass man z.B. als Alias in der _.bashrc_ hinzufügen kann. Das Skript darf nicht aus dem Ordner entfernt werden, da der Pfad zur CoderDojo Vorlage (_../_) darin hartcodiert ist.



Der Konvertierungsbefehl sieht so aus:
```
pandoc $in --filter $DIR/minted.py -o $output/$out --template=$DIR/pandoc_template.tex --variable vorlagen_pfad=$DIR/.. -s --smart 

pdflatex -interaction=nonstopmode -output-dir=$output -shell-escape $output/$out > $output/compile.log
```

wobei `$DIR` der Ordner ist, indem das Skript liegt, `$in` das Markdown-Dokument und `$output/$out` das Ausgabeverzeichnis und Ausgabedateiname ist.

Als Vorlage wird _pandoc_template.tex_ verwendet und der Pfad zur CoderDojo Latex-Vorlage muss angegeben werden.

**Achtung:** Enthält das Markdown-Dokument Codeblöck, so findet die verwendete _minted_-Umgebung in Latex die _pygments_-Dateien nicht, wenn die `-output-dir`gesetzt ist! Aus diesem Grund muss im Yaml-Header der Markdown-Datei (oder mittels --variable) die Variable: `minted_ausgabe=$output` gesetzt werden!