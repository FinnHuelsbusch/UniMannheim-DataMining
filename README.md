# Feature Selection

Feature die entfernt werden: 

| Feature  | Begründung                                                   | Aussage des Features                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| id       | Irrelevant                                                   |                                                              |
| ccf      | Konstant nur 0                                               | social security number                                       |
| pncaden  | Ist in den anderen Featuren bereits enthalten. (annahme: doppelt ist nicht besser, die Modelle können das selber) | (sum of painloc, painexer, relrest)                          |
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
| pro      | s.o.                                                         | Ob der Proband während des EKGs Diuretikum genommen hat      |
| proto    | s.o.                                                         | Welche Art von Belastungstest während der Erhebung verwendet wurde |
| thaldur  | s.o                                                          | Dauer der Belastungsmessung in minuten                       |
| thaltime | s.o.                                                         | Wann die Messung gestartet wurde                             |
| met      | Die Werte stimmen nicht mit realistischen Werten überein.    | Metabolisches Äquivalent gibt an wie gut der Körper mit Belastungen umgehen kann |

Featrue die zur Diskussion stehen 

| Feature  | Pro                                                          | Kontra                                                       | Aussage des Features                               |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------- |
| painloc  | Scheint relevant zu sein                                     | Viele Werte fehlen 31,5 % (cleveland)                        | Wo ist der Schmerz (1 = substernal; 0 = otherwise) |
| painexer | Scheint relevant zu sein                                     | Viele Werte fehlen 31,5 % (cleveland)                        | Schmerz bei Belastung 1 = ja 0 = nein              |
| relrest  | Scheint relevant zu sein                                     | Viele Werte fehlen 31,5 % (cleveland)                        | Schmerz geht zurück bei entspannung 1=ja 2=nein    |
| trestbps | Scheint relevant zu sein                                     | Werte Fehlen 6,8% (long-beach-va)   Unschlüssige Werte: 0    | Blutdruck                                          |
| htn      |                                                              | Wert ist nicht erklärbar/ Bedeutung unbekannt  4% fehlen vor allem in switzerland |                                                    |
| chol     | Scheint relevant zu sein   Ist in den 14 normalen Daten enthalten | 3.6 % fehlen vor allem in Ungarn   50 sind null in long beach   123 switzerland |                                                    |
| smoke    | Wir sind daran interessiert                                  | Normal fehlen 74 % nach Kombination mit years sind es nur noch 43% nach der Kombination mit years und cigs sind es 42% |                                                    |
| fbs      | Scheint relevant zu sein                                     | 10% fehlen vorallem in der Schweiz                           | Erhöhter Blutzucker  1 = ja 0 = nein               |

Feature die behalten werden: 

| Feature | Bemerkung                           | Aussage des Features                                         |
| ------- | ----------------------------------- | ------------------------------------------------------------ |
| age     | Nicht korrekt verteilt              | Alter                                                        |
| sex     | Nicht korrekt verteilt              | 1 = Männlich; 0 = Weiblich                                   |
| cp      | muss noch mit oneHot encoded werden | Schmerz typ:<br />- 1: typical angina<br />- 2: atypical angina<br />- 3: non-anginal pain<br />- 4: asymptomatic |
| restecg | muss noch mit oneHot encoded werden | - Value 0: normal<br />- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)<br />- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria |