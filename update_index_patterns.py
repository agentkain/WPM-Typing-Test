import os

file_path = r"c:\Users\ChiOnyeabor\OneDrive - Saddle Rock Legal Group\Desktop\WPM-Typing-Test\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_string = """            document.getElementById('custom-add-problematic-patterns').disabled = false;
            container.innerHTML = patterns.map(p => `
                <span style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px; font-size: 14px;">
                    <strong>"${p.pattern}"</strong>
                </span>
            `).join('');"""

replacement_code = """            document.getElementById('custom-add-problematic-patterns').style.display = 'none'; // Hide the bulk add button
            container.innerHTML = patterns.map(p => `
                <div style="background: rgba(0,0,0,0.1); padding: 5px 10px; border-radius: 4px; display: flex; align-items: center; gap: 10px;">
                    <span><strong>"${p.pattern}"</strong> (Score: ${p.score.toFixed(1)})</span>
                    <button class="add-pattern-btn" data-pattern="${p.pattern}" style="padding: 2px 8px; font-size: 12px; cursor: pointer; background-color: #34495e; color: white; border: none; border-radius: 3px;">Add</button>
                </div>
            `).join('');

            // Add event listeners to the new buttons
            container.querySelectorAll('.add-pattern-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    const pattern = this.getAttribute('data-pattern');
                    const customTextInput = document.getElementById('custom-text-input');
                    
                    // Generate words for this specific pattern
                    const allWords = [...beginnerWords, ...intermediateWords, ...advancedWords];
                    const matchingWords = allWords.filter(word => word.toLowerCase().includes(pattern.toLowerCase()));
                    // Take up to 10 words for this pattern
                    const patternWords = matchingWords.sort(() => Math.random() - 0.5).slice(0, 10);
                    
                    const currentWords = customTextInput.value.split(/\\s+/).filter(w => w.length > 0);
                    const newWords = [...currentWords, ...patternWords].slice(0, 100);
                    customTextInput.value = newWords.join(' ');
                });
            });"""

if target_string in content:
    new_content = content.replace(target_string, replacement_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated index.html")
else:
    print("Target string not found")
    # Print the area where we expect it to be to debug
    start_index = content.find("document.getElementById('custom-add-problematic-patterns').disabled = false;")
    if start_index != -1:
        print("Found partial match, surrounding context:")
        print(repr(content[start_index:start_index+300]))
