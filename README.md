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
| macro avg | 0.811     | 0.788  | 0.795    |


*Note*: These are the average of the values *per fold*, so *macro avg* is the average of the macro average of all categories per fold.

### Per-Category Metrics

| Category                                               | precision | recall | f1-score | support |
| ------------------------------------------------------ | --------- | ------ | -------- | ------- |
| AGGRAVATED ASSAULT                                     | 0.95      | 0.957  | 0.954    | 4085    |
| ARMED ROBBERY                                          | 0.958     | 0.957  | 0.957    | 1021    |
| ARSON                                                  | 0.951     | 0.953  | 0.952    | 344     |
| ASSAULTING PUBLIC OFFICER                              | 0.921     | 0.905  | 0.913    | 588     |
| AUTO THEFT                                             | 0.962     | 0.963  | 0.963    | 1660    |
| BLACKMAIL/EXTORTION/INTIMIDATION                       | 0.868     | 0.878  | 0.873    | 627     |
| BRIBERY AND CONFLICT OF INTEREST                       | 0.772     | 0.821  | 0.795    | 216     |
| BURGLARY                                               | 0.982     | 0.98   | 0.981    | 2214    |
| CHILD ABUSE                                            | 0.793     | 0.776  | 0.784    | 139     |
| COCAINE OR CRACK VIOLATION OFFENSE UNSPECIFIED         | 0.868     | 0.865  | 0.866    | 47      |
| COMMERCIALIZED VICE                                    | 0.811     | 0.777  | 0.793    | 666     |
| CONTEMPT OF COURT                                      | 0.983     | 0.987  | 0.985    | 2952    |
| CONTRIBUTING TO DELINQUENCY OF A MINOR                 | 0.454     | 0.379  | 0.396    | 50      |
| CONTROLLED SUBSTANCE - OFFENSE UNSPECIFIED             | 0.839     | 0.78   | 0.808    | 280     |
| COUNTERFEITING (FEDERAL ONLY)                          | 0         | 0      | 0        | 2       |
| DESTRUCTION OF PROPERTY                                | 0.967     | 0.97   | 0.969    | 2560    |
| DRIVING UNDER INFLUENCE - DRUGS                        | 0.641     | 0.616  | 0.625    | 34      |
| DRIVING UNDER THE INFLUENCE                            | 0.944     | 0.95   | 0.947    | 2195    |
| DRIVING WHILE INTOXICATED                              | 0.99      | 0.978  | 0.984    | 2391    |
| DRUG OFFENSES - VIOLATION/DRUG UNSPECIFIED             | 0.905     | 0.911  | 0.908    | 3100    |
| DRUNKENNESS/VAGRANCY/DISORDERLY CONDUCT                | 0.853     | 0.862  | 0.857    | 380     |
| EMBEZZLEMENT                                           | 0.86      | 0.762  | 0.808    | 100     |
| EMBEZZLEMENT (FEDERAL ONLY)                            | 0         | 0      | 0        | 1       |
| ESCAPE FROM CUSTODY                                    | 0.989     | 0.99   | 0.99     | 4035    |
| FAMILY RELATED OFFENSES                                | 0.744     | 0.768  | 0.756    | 442     |
| FELONY - UNSPECIFIED                                   | 0.665     | 0.762  | 0.709    | 122     |
| FLIGHT TO AVOID PROSECUTION                            | 0.43      | 0.434  | 0.431    | 38      |
| FORCIBLE SODOMY                                        | 0.773     | 0.837  | 0.802    | 76      |
| FORGERY (FEDERAL ONLY)                                 | 0         | 0      | 0        | 2       |
| FORGERY/FRAUD                                          | 0.909     | 0.928  | 0.918    | 4687    |
| FRAUD (FEDERAL ONLY)                                   | 0         | 0      | 0        | 2       |
| GRAND LARCENY - THEFT OVER $200                        | 0.959     | 0.972  | 0.966    | 2412    |
| HABITUAL OFFENDER                                      | 0.748     | 0.656  | 0.695    | 53      |
| HEROIN VIOLATION - OFFENSE UNSPECIFIED                 | 0.877     | 0.777  | 0.82     | 24      |
| HIT AND RUN DRIVING                                    | 0.927     | 0.933  | 0.93     | 303     |
| HIT/RUN DRIVING - PROPERTY DAMAGE                      | 0.929     | 0.924  | 0.926    | 362     |
| IMMIGRATION VIOLATIONS                                 | 0.778     | 0.616  | 0.681    | 19      |
| INVASION OF PRIVACY                                    | 0.925     | 0.923  | 0.924    | 1235    |
| JUVENILE OFFENSES                                      | 0.9       | 0.871  | 0.883    | 144     |
| KIDNAPPING                                             | 0.926     | 0.929  | 0.927    | 553     |
| LARCENY/THEFT - VALUE UNKNOWN                          | 0.953     | 0.946  | 0.95     | 3175    |
| LEWD ACT WITH CHILDREN                                 | 0.786     | 0.846  | 0.814    | 596     |
| LIQUOR LAW VIOLATIONS                                  | 0.731     | 0.762  | 0.746    | 214     |
| MANSLAUGHTER - NON-VEHICULAR                           | 0.661     | 0.803  | 0.725    | 139     |
| MANSLAUGHTER - VEHICULAR                               | 0.763     | 0.854  | 0.803    | 117     |
| MARIJUANA/HASHISH VIOLATION - OFFENSE UNSPECIFIED      | 0.778     | 0.675  | 0.718    | 62      |
| MISDEMEANOR UNSPECIFIED                                | 0.616     | 0.256  | 0.357    | 57      |
| MORALS/DECENCY - OFFENSE                               | 0.759     | 0.763  | 0.761    | 412     |
| MURDER                                                 | 0.965     | 0.922  | 0.943    | 621     |
| OBSTRUCTION - LAW ENFORCEMENT                          | 0.945     | 0.947  | 0.946    | 4220    |
| OFFENSES AGAINST COURTS, LEGISLATURES, AND COMMISSIONS | 0.882     | 0.897  | 0.889    | 1965    |
| PAROLE VIOLATION                                       | 0.968     | 0.949  | 0.958    | 946     |
| PETTY LARCENY - THEFT UNDER $200                       | 0.987     | 0.768  | 0.864    | 139     |
| POSSESSION/USE - COCAINE OR CRACK                      | 0.9       | 0.928  | 0.913    | 68      |
| POSSESSION/USE - DRUG UNSPECIFIED                      | 0.618     | 0.561  | 0.586    | 189     |
| POSSESSION/USE - HEROIN                                | 0.917     | 0.839  | 0.876    | 25      |
| POSSESSION/USE - MARIJUANA/HASHISH                     | 0.975     | 0.973  | 0.974    | 556     |
| POSSESSION/USE - OTHER CONTROLLED SUBSTANCES           | 0.976     | 0.965  | 0.97     | 3271    |
| PROBATION VIOLATION                                    | 0.958     | 0.956  | 0.957    | 1158    |
| PROPERTY OFFENSES - OTHER                              | 0.892     | 0.863  | 0.878    | 446     |
| PUBLIC ORDER OFFENSES - OTHER                          | 0.706     | 0.717  | 0.711    | 1871    |
| RACKETEERING/EXTORTION (FEDERAL ONLY)                  | 0         | 0      | 0        | 2       |
| RAPE - FORCE                                           | 0.841     | 0.871  | 0.856    | 641     |
| RAPE - STATUTORY - NO FORCE                            | 0.714     | 0.551  | 0.619    | 140     |
| REGULATORY OFFENSES (FEDERAL ONLY)                     | 0.8       | 0.558  | 0.657    | 70      |
| RIOTING                                                | 0.785     | 0.605  | 0.68     | 119     |
| SEXUAL ASSAULT - OTHER                                 | 0.829     | 0.839  | 0.834    | 971     |
| SIMPLE ASSAULT                                         | 0.977     | 0.967  | 0.972    | 4577    |
| STOLEN PROPERTY - RECEIVING                            | 0.953     | 0.955  | 0.954    | 1193    |
| STOLEN PROPERTY - TRAFFICKING                          | 0.899     | 0.875  | 0.887    | 491     |
| TAX LAW (FEDERAL ONLY)                                 | 0.474     | 0.177  | 0.256    | 30      |
| TRAFFIC OFFENSES - MINOR                               | 0.976     | 0.975  | 0.975    | 8699    |
| TRAFFICKING - COCAINE OR CRACK                         | 0.893     | 0.944  | 0.918    | 185     |
| TRAFFICKING - DRUG UNSPECIFIED                         | 0.729     | 0.783  | 0.755    | 516     |
| TRAFFICKING - HEROIN                                   | 0.874     | 0.902  | 0.887    | 54      |
| TRAFFICKING - OTHER CONTROLLED SUBSTANCES              | 0.963     | 0.953  | 0.958    | 2832    |
| TRAFFICKING MARIJUANA/HASHISH                          | 0.919     | 0.934  | 0.926    | 255     |
| TRESPASSING                                            | 0.974     | 0.982  | 0.978    | 1916    |
| UNARMED ROBBERY                                        | 0.941     | 0.935  | 0.938    | 377     |
| UNAUTHORIZED USE OF VEHICLE                            | 0.929     | 0.911  | 0.92     | 304     |
| UNSPECIFIED HOMICIDE                                   | 0.641     | 0.591  | 0.614    | 60      |
| VIOLENT OFFENSES - OTHER                               | 0.82      | 0.817  | 0.818    | 606     |
| VOLUNTARY/NONNEGLIGENT MANSLAUGHTER                    | 0.641     | 0.559  | 0.596    | 54      |
| WEAPON OFFENSE                                         | 0.944     | 0.947  | 0.945    | 2466    |

*Note: `support` is the average number of observations predicted on per fold, so the total number of observations per class is roughly 3x `support`.*

### Using Confidence Scores

If we interpret the classification probability as a confidence score, we can use it to filter out predictions that the model isn't as confident about. We applied this process in 3-fold cross validation. The numbers presented below indicate how much of the prediction data is retained given a confidence score cutoff of `p`. We present the overall accuracy and MCC metrics as if the model was only evaluated on this subset of confident predictions.

|     | cutoff | percent retained | mcc   | acc   |
| --- | ------ | ---------------- | ----- | ----- |
| 0   | 0.85   | 0.952            | 0.959 | 0.961 |
| 1   | 0.90   | 0.944            | 0.963 | 0.965 |
| 2   | 0.95   | 0.928            | 0.969 | 0.971 |
| 3   | 0.975  | 0.912            | 0.975 | 0.976 |
| 4   | 0.99   | 0.885            | 0.982 | 0.983 |
| 5   | 0.999  | 0.737            | 0.996 | 0.996 |