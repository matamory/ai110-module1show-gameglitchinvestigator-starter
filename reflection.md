# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I get a page that is titled Game Glitch Investigator and below that a heading that reads "Make a guess" with some directions that say "Guess a number between 1 and 100. Attempts left: 7". Then I see developer information and the interface for making a guess. Settings are on the left hand side and include adjustments for difficulty, range of numbers, and total attempts allowed. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  Number of attempts left does not seem to be consistent with actual number of attempts allowed. Appears to be off by at least least 1 value. 
  Hints do not coincide with guess and secret value. For example, if a value is 35 and user guesses 10, the hint tends to say "go lower". Unable to restart game using "New Game button". 
  

| Bug Found | Expected | Actual | Error/Output |
| ---------- | -------- | ------ | ------------ |
| Wrong hints | Go higher/lower correctly | Hints were backwards | "Too high" on a low guess |
| Off-by-one attempts | Count should drop by 1 | Count looked wrong at first | No error, just wrong display |
| New Game reset | Reset board immediately | Old state sometimes stayed | No error, but reset felt broken |
| Debug click delay | Count each submit once | First click did not count right away | No error, just delayed submit |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot was used for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
