import os

file_path = r"c:\Users\ChiOnyeabor\OneDrive - Saddle Rock Legal Group\Desktop\WPM-Typing-Test\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_string = 'console.error("Generate Random Words button not found");\n                }'
replacement_code = """console.error("Generate Random Words button not found");
                }

                // Add event listener to the "Add to Custom Text" button for problematic patterns
                const addPatternsButton = document.getElementById('custom-add-problematic-patterns');
                if (addPatternsButton) {
                     // Clone to remove old listeners
                    const newBtn = addPatternsButton.cloneNode(true);
                    addPatternsButton.parentNode.replaceChild(newBtn, addPatternsButton);
                    
                    newBtn.addEventListener('click', function () {
                        const customTextInput = document.getElementById('custom-text-input');
                        const patterns = analyzeErrorPatterns().map(p => p.pattern);
                        
                        // Generate words for these patterns
                        const allWords = [...beginnerWords, ...intermediateWords, ...advancedWords];
                        let patternWords = [];
                        
                        patterns.forEach(pattern => {
                            const matchingWords = allWords.filter(word => word.toLowerCase().includes(pattern.toLowerCase()));
                            // Take up to 5 words per pattern
                            patternWords.push(...matchingWords.sort(() => Math.random() - 0.5).slice(0, 5));
                        });
                        
                        // Shuffle and limit
                        patternWords = patternWords.sort(() => Math.random() - 0.5).slice(0, 20);

                        const currentWords = customTextInput.value.split(/\s+/).filter(w => w.length > 0);
                        const newWords = [...currentWords, ...patternWords].slice(0, 100);
                        customTextInput.value = newWords.join(' ');
                    });
                }

                updateCustomTextModalProblematicPatterns();"""

if target_string in content:
    new_content = content.replace(target_string, replacement_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated index.html")
else:
    print("Target string not found")
    # Print the area where we expect it to be to debug
    start_index = content.find('Generate Random Words button not found')
    if start_index != -1:
        print("Found partial match, surrounding context:")
        print(repr(content[start_index-50:start_index+100]))
