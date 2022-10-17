# Feature Selection

Feature die entfernt werden: 

| Feature  | Begründung                                                   | Aussage des Features                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| id       | Irrelevant                                                   |                                                              |
| painloc  | Scheint relevant zu sein                                     | Viele Werte fehlen 31,5 % (cleveland)                        |
| painexer | Scheint relevant zu sein                                     | Viele Werte fehlen 31,5 % (cleveland)                        |
| relrest  | Scheint relevant zu sein                                     | Viele Werte fehlen 31,5 % (cleveland)                        |
| ccf      | Konstant nur 0                                               | social security number                                       |
| pncaden  | Ist in den anderen Featuren bereits enthalten. (annahme: doppelt ist nicht besser, die Modelle können das selber) | (sum of painloc, painexer, relrest)                          |
| chol     | 20% Der werte enthalten 0 als Wert -> ungesund               | Cholesterinwert                                              |
| smoke    | Normal fehlen 74 % nach Kombination mit years sind es nur noch 43% nach der Kombination mit years und cigs sind es 42% | Raucher oder nicht raucher                                   |
| years    | Kombiniert mit smoke                                         | Jahre als raucher                                            |
| cigs     | Kombiniert mit smoke                                         | Anzahl an Zigaretten                                         |
| dm       | Zu viele fehlen 90%                                          |                                                              |
| famhist  | Zu viele fehlen 50%                                          | Erkrankung in der Familie                                    |
| ekgmo    | Ein Datum ist für das Modell eigentlich unerheblich. Besonders, da die Zeiträume zu kurz sind, um vernünftige Trends abzuleiten. Kann eventuell trotzdem mal interessant sein dort rein zu schauen | Monat, in dem das EKG geschrieben wurde                      |
| ekgday   | s.o.                                                         | Tag, in dem das EKG geschrieben wurde                        |
| ekgyr    | s.o.                                                         | Jahr, in dem das EKG geschrieben wurde                       |
| dig      | Die Art der Datenerhebung ist für uns irrelevant             | Ob beim EKG ein Herzglykoside verwendet wurden https://de.wikipedia.org/wiki/Herzglykoside |
| prop     | s.o.                                                         | Ob der Proband während des EKGs Betablocker genommen hat     |
| nitr     | s.o.                                                         | Ob der Proband während des EKGs Nitrate genommen hat         |
| diuretic | s.o.                                                         | Ob der Proband während des EKGs Diuretikum genommen hat      |
| proto    | s.o.                                                         | Welche Art von Belastungstest während der Erhebung verwendet wurde |
| thaldur  | s.o                                                          | Dauer der Belastungsmessung in minuten                       |
| thaltime | s.o.                                                         | Wann die Messung gestartet wurde                             |
| dummy    | Keine Erklärung der Bedeutung                                |                                                              |
| xhypo    | Unbekannte Bedeutung                                         | Unbekannte Bedeutung                                         |
| slope    | 30% fehlen                                                   | Art der ST Strecke unter maximaler belastung                 |
| rldv5    | 47 % fehlen                                                  | höhe der Ausschläge des EKGs bei ruhe                        |
| ca       | 67 % fehlen                                                  | Anzahl der hauptvenen                                        |
| restckm  | irrelevant laut uci                                          |                                                              |
| exerckm  | Konstante                                                    |                                                              |
| restef   | 97 % fehlen                                                  | Ich  studiere nicht Medizin kein plan                        |
| restwm   | s.o.                                                         | s.o.                                                         |
| exeref   | 99% Missing                                                  |                                                              |
| exerwm   | s.o.                                                         | s.o.                                                         |
| thal     | 53 %                                                         | s.o.                                                         |
| thalsev  | 85 %                                                         |                                                              |
| thalpul  | 95%                                                          |                                                              |
| earlobe  | not used laut uci                                            |                                                              |
| cmo      | Ein Datum ist für das Modell eigentlich unerheblich. Besonders, da die Zeiträume zu kurz sind, um vernünftige Trends abzuleiten. Kann eventuell trotzdem mal interessant sein dort rein zu schauen | datum (Monat)                                                |
| cday     | s.o.                                                         | datum (Jahr)                                                 |
| cyr      | s.o.                                                         | datum (Jahr)                                                 |
| lmt      | Kann mir nichts daraus ableiten und viele Werte fehlen       |                                                              |
| ladprox  | s.o.                                                         |                                                              |
| laddist  | s.o.                                                         |                                                              |
| diag     | s.o.                                                         |                                                              |
| cxmain   | s.o.                                                         |                                                              |
| ramus    | s.o.                                                         |                                                              |
| om1      | s.o.                                                         |                                                              |
| om2      | s.o.                                                         |                                                              |
| rcaprox  | s.o.                                                         |                                                              |
| rcadist  | s.o.                                                         |                                                              |
| lvx1     | not used by uci                                              |                                                              |
| lvx2     | not used by uci                                              |                                                              |
| lvx3     | not used by uci                                              |                                                              |
| lvx4     | not used by uci                                              |                                                              |
| lvf      | not used by uci                                              |                                                              |
| cathef   | not used by uci                                              |                                                              |
| junk     | not used by uci                                              |                                                              |
| name     | anonymisiert                                                 |                                                              |

Featrue die zur Diskussion stehen 

| Feature  | Pro                                                        | Kontra                                                       | Aussage des Features                                         |
| -------- | ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| trestbps | Scheint relevant zu sein                                   | Werte Fehlen 6,8% (long-beach-va)   Unschlüssige Werte: 0    | Blutdruck                                                    |
| htn      |                                                            | Wert ist nicht erklärbar/ Bedeutung unbekannt  4% fehlen vor allem in switzerland |                                                              |
| fbs      | Scheint relevant zu sein                                   | 10% fehlen vorallem in der Schweiz                           | Erhöhter Blutzucker  1 = ja 0 = nein                         |
| met      | eigentlich ein netter wert um die Belastbarkeit zu messen. | Die Werte stimmen nicht mit realistischen Werten überein.    | Metabolisches Äquivalent gibt an wie gut der Körper mit Belastungen umgehen kann |
| thalach  | Scheint sehr relevant zu sein                              | 57 fehlen in long beach                                      | maximum heart rate achieved                                  |
| thalrest | s.o                                                        | s.o                                                          | resting heart rate                                           |
| tpeakbps | s.o                                                        | s.o                                                          | peak exercise blood pressure (first of 2 parts)              |
| tpeakbpd | s.o                                                        | s.o                                                          | peak exercise blood pressure (second of 2 parts)             |
| trestbpd | s.o                                                        | s.o                                                          | resting blood pressure                                       |
| exang    | s.o                                                        | s.o                                                          | Übungen lösen Angina aus (Engegefühl in der Brust)           |
| oldpeak  | s.o                                                        | 57 fehlen in long beach                                      | Eine durch Belastung herbeigeführte ST-Senkung               |
| rldv5e   |                                                            | Nötige bearbeitung                                           | höhe des höchsten ausschlags des Belastungs ekgs             |

Feature die behalten werden, wenn NaN durch die Algorithmen gehandelt wer



Feature die behalten werden: 

| Feature | Bemerkung                           | Aussage des Features                                         |
| ------- | ----------------------------------- | ------------------------------------------------------------ |
| age     | Nicht korrekt verteilt              | Alter                                                        |
| sex     | Nicht korrekt verteilt              | 1 = Männlich; 0 = Weiblich                                   |
| cp      | muss noch mit oneHot encoded werden | Schmerz typ:<br />- 1: typical angina<br />- 2: atypical angina<br />- 3: non-anginal pain<br />- 4: asymptomatic |
| restecg | muss noch mit oneHot encoded werden | - Value 0: normal<br />- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)<br />- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria |
| num     | diagnosis of heart disease          |                                                              |