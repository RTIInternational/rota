---
language: 
- en
widget:
- text: theft 3
- text: forgery
- text: unlawful possession short-barreled shotgun
- text: criminal trespass 2nd degree
- text: eluding a police vehicle
- text: upcs synthetic narcotic
---

# ROTA
## Rapid Offense Text Autocoder

[![HuggingFace Models](https://img.shields.io/badge/%F0%9F%A4%97%20models-2021.05.17.14-blue)](https://huggingface.co/rti-international/rota)
[![GitHub Model Release](https://img.shields.io/github/v/release/RTIInternational/rota?logo=github)](https://github.com/RTIInternational/rota)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4739146.svg)](https://doi.org/10.5281/zenodo.4739146)

Criminal justice research often requires conversion of free-text offense descriptions into overall charge categories to aid analysis. For example, the free-text offense of "eluding a police vehicle" would be coded to a charge category of "Obstruction - Law Enforcement". Since free-text offense descriptions aren't standardized and often need to be categorized in large volumes, this can result in a manual and time intensive process for researchers. ROTA is a machine learning model for converting offense text into offense codes. 

Currently ROTA predicts the *Charge Category* of a given offense text. A *charge category* is one of the headings for offense codes in the [2009 NCRP Codebook: Appendix F](https://www.icpsr.umich.edu/web/NACJD/studies/30799/datadocumentation#).

The model was trained on [publicly available data](https://web.archive.org/web/20201021001250/https://www.icpsr.umich.edu/web/pages/NACJD/guides/ncrp.html) from a crosswalk containing offenses from all 50 states combined with three additional hand-labeled offense text datasets.

<details>
    <summary>Charge Category Example</summary>
    <img src="https://i.ibb.co/xLsrzmV/charge-category-example.png" width="500">
</details>

### Data Preprocessing

The input text is standardized through a series of preprocessing steps. The text is first passed through a sequence of 500+ case-insensitive regular expressions that identify common misspellings and abbreviations and expand the text to a more full, correct English text. Some data-specific prefixes and suffixes are then removed from the text -- e.g. some states included a statute as a part of the text. Finally, punctuation (excluding dollar signs) are removed from the input, multiple spaces between words are removed, and the text is lowercased. 

## Cross-Validation Performance

This model was evaluated using 3-fold cross validation. Except where noted, numbers presented below are the mean value across the 3 folds. 

The model in this repository is trained on all available data. Because of this, you can typically expect production performance to be (unknowably) better than the numbers presented below.

### Overall Metrics

| Metric   | Value |
| -------- | ----- |
| Accuracy | 0.934 |
| MCC      | 0.931 |

 

| Metric    | precision | recall | f1-score |
| --------- | --------- | ------ | -------- |
| macro avg | 0.811     | 0.786  | 0.794    |


*Note*: These are the average of the values *per fold*, so *macro avg* is the average of the macro average of all categories per fold.

### Per-Category Metrics

| Category                                               | precision | recall | f1-score | support |
| ------------------------------------------------------ | --------- | ------ | -------- | ------- |
| AGGRAVATED ASSAULT                                     | 0.954     | 0.954  | 0.954    | 4085    |
| ARMED ROBBERY                                          | 0.961     | 0.955  | 0.958    | 1021    |
| ARSON                                                  | 0.946     | 0.954  | 0.95     | 344     |
| ASSAULTING PUBLIC OFFICER                              | 0.914     | 0.905  | 0.909    | 588     |
| AUTO THEFT                                             | 0.962     | 0.962  | 0.962    | 1660    |
| BLACKMAIL/EXTORTION/INTIMIDATION                       | 0.872     | 0.871  | 0.872    | 627     |
| BRIBERY AND CONFLICT OF INTEREST                       | 0.784     | 0.796  | 0.79     | 216     |
| BURGLARY                                               | 0.979     | 0.981  | 0.98     | 2214    |
| CHILD ABUSE                                            | 0.805     | 0.78   | 0.792    | 139     |
| COCAINE OR CRACK VIOLATION OFFENSE UNSPECIFIED         | 0.827     | 0.815  | 0.821    | 47      |
| COMMERCIALIZED VICE                                    | 0.818     | 0.788  | 0.802    | 666     |
| CONTEMPT OF COURT                                      | 0.982     | 0.987  | 0.984    | 2952    |
| CONTRIBUTING TO DELINQUENCY OF A MINOR                 | 0.544     | 0.333  | 0.392    | 50      |
| CONTROLLED SUBSTANCE - OFFENSE UNSPECIFIED             | 0.864     | 0.791  | 0.826    | 280     |
| COUNTERFEITING (FEDERAL ONLY)                          | 0         | 0      | 0        | 2       |
| DESTRUCTION OF PROPERTY                                | 0.97      | 0.968  | 0.969    | 2560    |
| DRIVING UNDER INFLUENCE - DRUGS                        | 0.567     | 0.603  | 0.581    | 34      |
| DRIVING UNDER THE INFLUENCE                            | 0.951     | 0.946  | 0.949    | 2195    |
| DRIVING WHILE INTOXICATED                              | 0.986     | 0.981  | 0.984    | 2391    |
| DRUG OFFENSES - VIOLATION/DRUG UNSPECIFIED             | 0.903     | 0.911  | 0.907    | 3100    |
| DRUNKENNESS/VAGRANCY/DISORDERLY CONDUCT                | 0.856     | 0.861  | 0.858    | 380     |
| EMBEZZLEMENT                                           | 0.865     | 0.759  | 0.809    | 100     |
| EMBEZZLEMENT (FEDERAL ONLY)                            | 0         | 0      | 0        | 1       |
| ESCAPE FROM CUSTODY                                    | 0.988     | 0.991  | 0.989    | 4035    |
| FAMILY RELATED OFFENSES                                | 0.739     | 0.773  | 0.755    | 442     |
| FELONY - UNSPECIFIED                                   | 0.692     | 0.735  | 0.712    | 122     |
| FLIGHT TO AVOID PROSECUTION                            | 0.46      | 0.407  | 0.425    | 38      |
| FORCIBLE SODOMY                                        | 0.82      | 0.8    | 0.809    | 76      |
| FORGERY (FEDERAL ONLY)                                 | 0         | 0      | 0        | 2       |
| FORGERY/FRAUD                                          | 0.911     | 0.928  | 0.919    | 4687    |
| FRAUD (FEDERAL ONLY)                                   | 0         | 0      | 0        | 2       |
| GRAND LARCENY - THEFT OVER $200                        | 0.957     | 0.973  | 0.965    | 2412    |
| HABITUAL OFFENDER                                      | 0.742     | 0.627  | 0.679    | 53      |
| HEROIN VIOLATION - OFFENSE UNSPECIFIED                 | 0.879     | 0.811  | 0.843    | 24      |
| HIT AND RUN DRIVING                                    | 0.922     | 0.94   | 0.931    | 303     |
| HIT/RUN DRIVING - PROPERTY DAMAGE                      | 0.929     | 0.918  | 0.923    | 362     |
| IMMIGRATION VIOLATIONS                                 | 0.84      | 0.609  | 0.697    | 19      |
| INVASION OF PRIVACY                                    | 0.927     | 0.923  | 0.925    | 1235    |
| JUVENILE OFFENSES                                      | 0.928     | 0.866  | 0.895    | 144     |
| KIDNAPPING                                             | 0.937     | 0.93   | 0.933    | 553     |
| LARCENY/THEFT - VALUE UNKNOWN                          | 0.955     | 0.945  | 0.95     | 3175    |
| LEWD ACT WITH CHILDREN                                 | 0.775     | 0.85   | 0.811    | 596     |
| LIQUOR LAW VIOLATIONS                                  | 0.741     | 0.768  | 0.755    | 214     |
| MANSLAUGHTER - NON-VEHICULAR                           | 0.626     | 0.802  | 0.701    | 139     |
| MANSLAUGHTER - VEHICULAR                               | 0.79      | 0.853  | 0.819    | 117     |
| MARIJUANA/HASHISH VIOLATION - OFFENSE UNSPECIFIED      | 0.741     | 0.662  | 0.699    | 62      |
| MISDEMEANOR UNSPECIFIED                                | 0.63      | 0.243  | 0.347    | 57      |
| MORALS/DECENCY - OFFENSE                               | 0.774     | 0.764  | 0.769    | 412     |
| MURDER                                                 | 0.965     | 0.915  | 0.939    | 621     |
| OBSTRUCTION - LAW ENFORCEMENT                          | 0.939     | 0.947  | 0.943    | 4220    |
| OFFENSES AGAINST COURTS, LEGISLATURES, AND COMMISSIONS | 0.881     | 0.895  | 0.888    | 1965    |
| PAROLE VIOLATION                                       | 0.97      | 0.953  | 0.962    | 946     |
| PETTY LARCENY - THEFT UNDER $200                       | 0.965     | 0.761  | 0.85     | 139     |
| POSSESSION/USE - COCAINE OR CRACK                      | 0.893     | 0.928  | 0.908    | 68      |
| POSSESSION/USE - DRUG UNSPECIFIED                      | 0.624     | 0.535  | 0.572    | 189     |
| POSSESSION/USE - HEROIN                                | 0.884     | 0.852  | 0.866    | 25      |
| POSSESSION/USE - MARIJUANA/HASHISH                     | 0.977     | 0.97   | 0.973    | 556     |
| POSSESSION/USE - OTHER CONTROLLED SUBSTANCES           | 0.975     | 0.965  | 0.97     | 3271    |
| PROBATION VIOLATION                                    | 0.963     | 0.953  | 0.958    | 1158    |
| PROPERTY OFFENSES - OTHER                              | 0.901     | 0.87   | 0.885    | 446     |
| PUBLIC ORDER OFFENSES - OTHER                          | 0.7       | 0.721  | 0.71     | 1871    |
| RACKETEERING/EXTORTION (FEDERAL ONLY)                  | 0         | 0      | 0        | 2       |
| RAPE - FORCE                                           | 0.842     | 0.873  | 0.857    | 641     |
| RAPE - STATUTORY - NO FORCE                            | 0.707     | 0.55   | 0.611    | 140     |
| REGULATORY OFFENSES (FEDERAL ONLY)                     | 0.847     | 0.567  | 0.674    | 70      |
| RIOTING                                                | 0.784     | 0.605  | 0.68     | 119     |
| SEXUAL ASSAULT - OTHER                                 | 0.836     | 0.836  | 0.836    | 971     |
| SIMPLE ASSAULT                                         | 0.976     | 0.967  | 0.972    | 4577    |
| STOLEN PROPERTY - RECEIVING                            | 0.959     | 0.957  | 0.958    | 1193    |
| STOLEN PROPERTY - TRAFFICKING                          | 0.902     | 0.888  | 0.895    | 491     |
| TAX LAW (FEDERAL ONLY)                                 | 0.373     | 0.233  | 0.286    | 30      |
| TRAFFIC OFFENSES - MINOR                               | 0.974     | 0.977  | 0.976    | 8699    |
| TRAFFICKING - COCAINE OR CRACK                         | 0.896     | 0.951  | 0.922    | 185     |
| TRAFFICKING - DRUG UNSPECIFIED                         | 0.709     | 0.795  | 0.749    | 516     |
| TRAFFICKING - HEROIN                                   | 0.871     | 0.92   | 0.894    | 54      |
| TRAFFICKING - OTHER CONTROLLED SUBSTANCES              | 0.963     | 0.954  | 0.959    | 2832    |
| TRAFFICKING MARIJUANA/HASHISH                          | 0.921     | 0.943  | 0.932    | 255     |
| TRESPASSING                                            | 0.974     | 0.98   | 0.977    | 1916    |
| UNARMED ROBBERY                                        | 0.941     | 0.939  | 0.94     | 377     |
| UNAUTHORIZED USE OF VEHICLE                            | 0.94      | 0.908  | 0.924    | 304     |
| UNSPECIFIED HOMICIDE                                   | 0.61      | 0.554  | 0.577    | 60      |
| VIOLENT OFFENSES - OTHER                               | 0.827     | 0.817  | 0.822    | 606     |
| VOLUNTARY/NONNEGLIGENT MANSLAUGHTER                    | 0.619     | 0.513  | 0.542    | 54      |
| WEAPON OFFENSE                                         | 0.943     | 0.949  | 0.946    | 2466    |

*Note: `support` is the average number of observations predicted on per fold, so the total number of observations per class is roughly 3x `support`.*

### Using Confidence Scores

If we interpret the classification probability as a confidence score, we can use it to filter out predictions that the model isn't as confident about. We applied this process in 3-fold cross validation. The numbers presented below indicate how much of the prediction data is retained given a confidence score cutoff of `p`. We present the overall accuracy and MCC metrics as if the model was only evaluated on this subset of confident predictions.

|     | cutoff | percent retained | mcc   | acc   |
| --- | ------ | ---------------- | ----- | ----- |
| 0   | 0.85   | 0.952            | 0.96  | 0.961 |
| 1   | 0.9    | 0.943            | 0.964 | 0.965 |
| 2   | 0.95   | 0.928            | 0.97  | 0.971 |
| 3   | 0.975  | 0.912            | 0.975 | 0.976 |
| 4   | 0.99   | 0.886            | 0.982 | 0.983 |
| 5   | 0.999  | 0.733            | 0.995 | 0.996 |