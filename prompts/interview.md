<!-- Same text as .claude/commands/interview.md, for tools other than Claude Code. Paste it into your AI tool; where Claude Code fills in $ARGUMENTS, write your request yourself. -->

Requirements interview.

Use only the context I give you: my message and any file or notes I attach. Do not open other files unless I point you to them. Do not write any code.

My notes may already decide most things: input and output, edge cases, the algorithm, the expected cost. Do not ask about anything they already answer. Ask only about what is still open: a word that can be read two ways, a case my notes do not cover, a step that could be carried out in two different ways, a limit that is not stated.

Ask one question per turn, in this format and nothing more:

Question N: <one sentence>
<one or two plain sentences on why it matters for the code>
Options:
- A. <possible answer> (recommended: <reason in a few words>)
- B. <possible answer>
- (more letters if there are more real choices; list every answer that a reasonable person might give, usually two to four)
- Other (tell me)

Mark exactly one option as recommended, with the reason in a few words; put it first. Use short sentences. Do not repeat what my notes say, do not list what you would assume, and do not add commentary. Stop and wait for my answer. After I answer, ask the next question. When nothing is left, write a short list titled "Decisions from the interview", one line per question with my answer, then end with the line "Ready to write a spec." and stop. If my notes leave nothing open, say so, then end with the same line and stop.

Language: reply in the language I write in. If I write in Korean, write your answers and any Markdown file you create (the specification included, section titles too) in Korean. Code, identifiers, and comments stay in English.

What I want to build: (write it here, and paste or attach your design notes)
