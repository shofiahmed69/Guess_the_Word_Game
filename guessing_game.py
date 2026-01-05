import tkinter as tk
from tkinter import messagebox
import random

# Word lists with more variety
easy_words = ["apple", "vanilla", "cat", "dog", "money", "book", "tree", "sun", "moon", "star", 
              "fish", "bird", "home", "love", "time", "water", "fire", "wind", "rain", "snow"]

medium_words = ["python", "bomber", "archer", "husky", "html", "css", "guitar", "pizza", 
                "laptop", "coffee", "rocket", "jungle", "castle", "dragon", "wizard", "knight",
                "planet", "galaxy", "ocean", "mountain"]

hard_words = ["bootstrap", "flutter", "mechanic", "machoman", "darkknight", "beast", 
              "butterfly", "crocodile", "elephant", "kangaroo", "detective", "architect",
              "astronaut", "celebration", "technology", "championship", "revolutionary", 
              "extraordinary", "supernatural", "magnificent"]

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("650x550")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
        
        self.secret_word = ""
        self.attempts = 0
        self.max_attempts = 5  # Maximum 5 guesses
        self.total_score = 0  # Total score across all games
        self.game_started = False
        
        self.create_welcome_screen()
    
    def create_welcome_screen(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title = tk.Label(self.root, text="🎮 Word Guessing Game 🎮", 
                        font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=20)
        
        # Score display
        score_label = tk.Label(self.root, text=f"🏆 Total Score: {self.total_score}", 
                              font=("Arial", 18, "bold"), bg="#2c3e50", fg="#f39c12")
        score_label.pack(pady=5)
        
        # Subtitle
        subtitle = tk.Label(self.root, text="Choose Your Difficulty Level", 
                           font=("Arial", 16), bg="#2c3e50", fg="#bdc3c7")
        subtitle.pack(pady=10)
        
        # Rules info
        rules = tk.Label(self.root, text="⚠️ You have 5 attempts to guess the word!", 
                        font=("Arial", 12), bg="#2c3e50", fg="#e74c3c")
        rules.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=30)
        
        # Easy button
        easy_btn = tk.Button(button_frame, text="🟢 EASY\n(50 points)", font=("Arial", 14, "bold"),
                            bg="#27ae60", fg="white", width=15, height=3,
                            command=lambda: self.start_game("easy"), cursor="hand2",
                            relief="raised", bd=3)
        easy_btn.pack(pady=8)
        
        # Medium button
        medium_btn = tk.Button(button_frame, text="🟡 MEDIUM\n(100 points)", font=("Arial", 14, "bold"),
                              bg="#f39c12", fg="white", width=15, height=3,
                              command=lambda: self.start_game("medium"), cursor="hand2",
                              relief="raised", bd=3)
        medium_btn.pack(pady=8)
        
        # Hard button
        hard_btn = tk.Button(button_frame, text="🔴 HARD\n(200 points)", font=("Arial", 14, "bold"),
                            bg="#e74c3c", fg="white", width=15, height=3,
                            command=lambda: self.start_game("hard"), cursor="hand2",
                            relief="raised", bd=3)
        hard_btn.pack(pady=8)
    
    def start_game(self, level):
        self.attempts = 0
        self.game_started = True
        
        # Choose random word and set points based on difficulty
        if level == "easy":
            self.secret_word = random.choice(easy_words)
            difficulty_color = "#27ae60"
            self.base_points = 50
        elif level == "medium":
            self.secret_word = random.choice(medium_words)
            difficulty_color = "#f39c12"
            self.base_points = 100
        else:
            self.secret_word = random.choice(hard_words)
            difficulty_color = "#e74c3c"
            self.base_points = 200
        
        self.create_game_screen(level, difficulty_color)
    
    def calculate_score(self):
        # Score calculation: Base points * (remaining attempts / max attempts)
        # Fewer attempts = higher score
        remaining = self.max_attempts - self.attempts + 1
        bonus_multiplier = remaining / self.max_attempts
        score = int(self.base_points * bonus_multiplier)
        return score
    
    def create_game_screen(self, level, color):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header frame
        header_frame = tk.Frame(self.root, bg=color, height=100)
        header_frame.pack(fill="x")
        
        # Title in header
        title = tk.Label(header_frame, text=f"Level: {level.upper()}", 
                        font=("Arial", 20, "bold"), bg=color, fg="white")
        title.pack(pady=10)
        
        # Info frame (attempts and score)
        info_frame = tk.Frame(header_frame, bg=color)
        info_frame.pack()
        
        # Attempts counter with remaining attempts
        attempts_remaining = self.max_attempts - self.attempts
        self.attempts_label = tk.Label(info_frame, 
                                      text=f"Attempts: {self.attempts}/{self.max_attempts} | Remaining: {attempts_remaining}", 
                                      font=("Arial", 13), bg=color, fg="white")
        self.attempts_label.pack(side="left", padx=10)
        
        # Current score display
        self.score_label = tk.Label(info_frame, text=f"🏆 Total Score: {self.total_score}", 
                                   font=("Arial", 13, "bold"), bg=color, fg="#f1c40f")
        self.score_label.pack(side="left", padx=10)
        
        # Main game frame
        game_frame = tk.Frame(self.root, bg="#34495e")
        game_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Instructions
        instruction = tk.Label(game_frame, text="Guess the secret word!", 
                              font=("Arial", 16), bg="#34495e", fg="#ecf0f1")
        instruction.pack(pady=15)
        
        # Word length hint
        length_hint = tk.Label(game_frame, text=f"💡 The word has {len(self.secret_word)} letters", 
                              font=("Arial", 13), bg="#34495e", fg="#3498db")
        length_hint.pack(pady=5)
        
        # Hint display
        hint_frame = tk.Frame(game_frame, bg="#2c3e50", relief="sunken", bd=2)
        hint_frame.pack(pady=20)
        
        self.hint_label = tk.Label(hint_frame, text="_" * len(self.secret_word), 
                                   font=("Courier", 28, "bold"), bg="#2c3e50", 
                                   fg="#3498db", padx=20, pady=15)
        self.hint_label.pack()
        
        # Input frame
        input_frame = tk.Frame(game_frame, bg="#34495e")
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Your Guess:", font=("Arial", 14), 
                bg="#34495e", fg="#ecf0f1").pack(side="left", padx=10)
        
        self.guess_entry = tk.Entry(input_frame, font=("Arial", 16), width=20, 
                                    bg="#ecf0f1", relief="solid", bd=2)
        self.guess_entry.pack(side="left", padx=10)
        self.guess_entry.focus()
        
        # Bind Enter key
        self.guess_entry.bind('<Return>', lambda e: self.check_guess())
        
        # Button frame
        btn_frame = tk.Frame(game_frame, bg="#34495e")
        btn_frame.pack(pady=20)
        
        # Submit button
        submit_btn = tk.Button(btn_frame, text="✓ Submit", font=("Arial", 14, "bold"),
                              bg="#3498db", fg="white", width=12, height=2,
                              command=self.check_guess, cursor="hand2", relief="raised", bd=3)
        submit_btn.pack(side="left", padx=10)
        
        # Back button
        back_btn = tk.Button(btn_frame, text="← Back", font=("Arial", 14, "bold"),
                            bg="#95a5a6", fg="white", width=12, height=2,
                            command=self.create_welcome_screen, cursor="hand2", 
                            relief="raised", bd=3)
        back_btn.pack(side="left", padx=10)
    
    def check_guess(self):
        guess = self.guess_entry.get().lower().strip()
        
        if not guess:
            messagebox.showwarning("Empty Guess", "Please enter a word!")
            return
        
        self.attempts += 1
        attempts_remaining = self.max_attempts - self.attempts
        
        # Update attempts label
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts} | Remaining: {attempts_remaining}")
        
        # Check if player won
        if guess == self.secret_word:
            earned_score = self.calculate_score()
            self.total_score += earned_score
            
            messagebox.showinfo("🎉 Congratulations!", 
                              f"You guessed it in {self.attempts} attempts!\n\n"
                              f"The word was: {self.secret_word.upper()}\n\n"
                              f"🌟 You earned: {earned_score} points!\n"
                              f"🏆 Total Score: {self.total_score}")
            self.create_welcome_screen()
            return
        
        # Check if player ran out of attempts
        if self.attempts >= self.max_attempts:
            messagebox.showerror("😞 Game Over!", 
                               f"You've used all {self.max_attempts} attempts!\n\n"
                               f"The word was: {self.secret_word.upper()}\n\n"
                               f"No points earned this round.\n"
                               f"🏆 Total Score: {self.total_score}")
            self.create_welcome_screen()
            return
        
        # Generate hint
        hint = ""
        for i in range(len(self.secret_word)):
            if i < len(guess) and guess[i] == self.secret_word[i]:
                hint += guess[i].upper()
            else:
                hint += "_"
        
        self.hint_label.config(text=hint)
        self.guess_entry.delete(0, tk.END)
        
        # Show feedback with remaining attempts
        if len(guess) != len(self.secret_word):
            messagebox.showinfo("Hint", 
                              f"Try again! The word has {len(self.secret_word)} letters.\n"
                              f"Attempts remaining: {attempts_remaining}")
        else:
            messagebox.showinfo("Keep trying!", 
                              f"Not quite! Check the hint.\n"
                              f"Attempts remaining: {attempts_remaining}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()