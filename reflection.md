# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game it appeared to work visually but immediately showed 
suspicious behavior during gameplay. The first major bug I noticed was that the 
hint direction was completely inverted — when I guessed 1 and the secret number 
was 8, it told me to "Go LOWER" instead of "Go HIGHER." The second bug was that 
the attempts counter started at 7 even though the settings panel clearly showed 
"Attempts allowed: 8," meaning the player loses one attempt before they even start. 
I also discovered the score went negative as guesses were made, and the game 
accepted inputs completely outside the 1-100 range, like -5 and 105.

---

## 2. How did you use AI as a teammate?

I used GitHub Copilot Chat and Copilot Agent Mode in VS Code. A correct 
suggestion was when Copilot Agent automatically identified all four bugs, 
refactored check_guess and parse_guess into logic_utils.py, and updated 
the imports in app.py — I verified this by running pytest and all 3 tests 
passed. A misleading suggestion was that Copilot did not initially fix the 
New Game button — it missed resetting session_state.status, score, and 
history, which I caught through manual gameplay testing.


---

## 3. Debugging and testing your fixes

I verified fixes by running pytest tests/ -v after each change and by 
manually playing the game in the browser. The pytest suite confirmed 
check_guess correctly returns "Too High"/"Too Low" with proper messages. 
Manual testing revealed the New Game bug that pytest didn't catch — showing 
the value of combining automated and manual testing. Copilot helped generate 
the initial test structure but I had to verify the expected values matched 
the fixed logic.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom every time a 
user interacts with the page — clicking a button, typing input, or changing 
a dropdown all trigger a full rerun. Session state is how Streamlit 
remembers information between those reruns, like the secret number, attempt 
count, and game status. Without session_state, every rerun would reset 
everything and the game couldn't function. I learned this firsthand when the 
New Game button wasn't resetting status — because session_state persists 
across reruns, forgetting to reset it meant the game stayed in "lost" state 
even after clicking New Game.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is adding FIXME comments before touching any code 
— marking the crime scene first helped me stay organized and gave Copilot 
clear targets to work with. Next time I work with AI on a coding task I 
would run manual tests immediately after AI makes changes instead of 
assuming the automated tests catch everything — Copilot missed the New Game 
reset bug entirely. This project changed how I think about AI-generated code 
because it showed me that AI can identify and fix bugs quickly but still 
misses edge cases that only surface through real user interaction.
