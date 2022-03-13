# step_counter

This is the wrapper with cloc for analyze github repositories.

# Usage

- Write repositories name in `repo_list.txt` what you want to analyze.
- Write your account name in `user.txt`
- Run `count_repo.py`

These step ended, it shows up looks like below result.

```
$ python3 count_repo.py
1 / 18 : env_web_viewer
2 / 18 : tetris_m5stack_core2
3 / 18 : sensing_and_display_AR
4 / 18 : checksamedir
5 / 18 : brainf-ck
6 / 18 : c_tetris_gui
7 / 18 : chat-apps
8 / 18 : mandelbrot
9 / 18 : knall
10 / 18 : FormulaGenerateUtility
11 / 18 : lifegame
12 / 18 : logic_proof_helper
13 / 18 : hslifegame-curses
14 / 18 : CC-Programs
15 / 18 : address_protector
16 / 18 : abc10946.github.io
17 / 18 : c_tetris
18 / 18 : hslifegame

github.com/AlDanial/cloc v 1.82
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
C                                6            170             30           1062
Python                          26            271             25            881
C++                              5             59             11            416
Haskell                         10             83              0            376
Markdown                        15            133              0            322
Lua                              5             28              4            262
C/C++ Header                     7            105              2            259
HTML                             6              6              2            105
JavaScript                       3             14              0            105
CSS                              1             24              0            100
Arduino Sketch                   1             12             10             58
YAML                             4             17            118             51
make                             3              9              0             30
JSON                             1              0              0             12
Dockerfile                       1              3              0              5
Brainfuck                        1              0              0              1
-------------------------------------------------------------------------------
SUM:                            95            934            202           4045
-------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------
File                                                        files          blank        comment           code
--------------------------------------------------------------------------------------------------------------
./reports/ABC10946_c_tetris_gui_report                          7            125              9            607
./reports/ABC10946_c_tetris_report                              4             90              8            474
./reports/ABC10946_tetris_m5stack_core2_report                  4             84             18            458
./reports/ABC10946_CC-Programs_report                           6             69              4            346
./reports/ABC10946_hslifegame_report                           10             66             63            279
./reports/ABC10946_logic_proof_helper_report                   13            113              0            263
./reports/ABC10946_FormulaGenerateUtility_report                5             63              0            215
./reports/ABC10946_env_web_viewer_report                        5             46              2            184
./reports/ABC10946_hslifegame-curses_report                     6             42             55            173
./reports/ABC10946_lifegame_report                              3             38              0            173
./reports/ABC10946_knall_report                                 1             33             13            172
./reports/ABC10946_abc10946.github.io_report                    3             28              0            147
./reports/ABC10946_brainf-ck_report                             3             37              2            142
./reports/ABC10946_chat-apps_report                             8             15              0            137
./reports/ABC10946_mandelbrot_report                            8             30              5            134
./reports/ABC10946_sensing_and_display_AR_report                4             40             23             96
./reports/ABC10946_checksamedir_report                          2             14              0             27
./reports/ABC10946_address_protector_report                     3              1              0             18
--------------------------------------------------------------------------------------------------------------
SUM:                                                           95            934            202           4045
--------------------------------------------------------------------------------------------------------------
```
