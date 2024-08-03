import random
import time

class Quiz:
    def __init__(self):
        self.categories = {
            "Math": [
                {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": 2},
                {"question": "What is 9 x 6?", "options": ["52", "54", "56", "58"], "answer": 1},
                {"question": "What is 15 divided by 3?", "options": ["4", "5", "6", "7"], "answer": 1},
                {"question": "What is 8 squared?", "options": ["64", "72", "80", "88"], "answer": 0},
                {"question": "What is the square root of 49?", "options": ["5", "6", "7", "8"], "answer": 2},
                {"question": "What is the value of π (pi) approximately?", "options": ["3.14", "2.71", "1.62", "1.41"], "answer": 0},
                {"question": "What is 100 - 37?", "options": ["63", "64", "65", "66"], "answer": 0},
                {"question": "What is 25% of 200?", "options": ["40", "45", "50", "55"], "answer": 2}
            ],
            "Science": [
                {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 1},
                {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": 0},
                {"question": "What is the process by which plants make their food?", "options": ["Photosynthesis", "Respiration", "Digestion", "Transpiration"], "answer": 0},
                {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], "answer": 1},
                {"question": "What is the boiling point of water in Celsius?", "options": ["90", "95", "100", "105"], "answer": 2},
                {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 2},
                {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": 2},
                {"question": "What is the name of the galaxy that contains our Solar System?", "options": ["Andromeda", "Milky Way", "Messier 87", "Triangulum"], "answer": 1}
            ],
            "History": [
                {"question": "Who was the first President of the United States?", "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "answer": 0},
                {"question": "In which year did World War I begin?", "options": ["1912", "1914", "1916", "1918"], "answer": 1},
                {"question": "Who was the famous queen of ancient Egypt?", "options": ["Cleopatra", "Nefertiti", "Hatshepsut", "Tutankhamun"], "answer": 0},
                {"question": "What ancient civilization built the Machu Picchu?", "options": ["Inca", "Aztec", "Maya", "Olmec"], "answer": 0},
                {"question": "Who was the leader of the Soviet Union during World War II?", "options": ["Joseph Stalin", "Vladimir Lenin", "Nikita Khrushchev", "Leon Trotsky"], "answer": 0},
                {"question": "What was the name of the ship that carried the Pilgrims to America in 1620?", "options": ["Mayflower", "Nina", "Pinta", "Santa Maria"], "answer": 0},
                {"question": "Who was the first man to walk on the moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"], "answer": 0},
                {"question": "What was the name of the treaty that ended World War I?", "options": ["Treaty of Versailles", "Treaty of Paris", "Treaty of Rome", "Treaty of Utrecht"], "answer": 0}
            ],
            "Literature": [
                {"question": "Who wrote '1984'?", "options": ["George Orwell", "Aldous Huxley", "J.K. Rowling", "H.G. Wells"], "answer": 0},
                {"question": "What is the name of the wizarding school in 'Harry Potter'?", "options": ["Hogwarts", "Beauxbatons", "Durmstrang", "Ilvermorny"], "answer": 0},
                {"question": "Who wrote 'Pride and Prejudice'?", "options": ["Jane Austen", "Charlotte Brontë", "Emily Dickinson", "Mary Shelley"], "answer": 0},
                {"question": "In which novel does the character Holden Caulfield appear?", "options": ["The Catcher in the Rye", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick"], "answer": 0},
                {"question": "Who is the author of 'The Hobbit'?", "options": ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"], "answer": 0},
                {"question": "Which novel starts with 'It was the best of times, it was the worst of times'?", "options": ["A Tale of Two Cities", "Great Expectations", "Oliver Twist", "David Copperfield"], "answer": 0},
                {"question": "Who wrote 'Brave New World'?", "options": ["Aldous Huxley", "George Orwell", "Ray Bradbury", "Isaac Asimov"], "answer": 0},
                {"question": "What is the name of the fictional country in 'The Hunger Games'?", "options": ["Panem", "Gilead", "Westeros", "Narnia"], "answer": 0}
            ]
        }
        self.score = 0
        self.leaderboard = []

    def start(self):
        print("WELCOME!!!")

        while True:
            print("\nCategories:")
            for category in self.categories:
                print(f"- {category}")
            category = input("CHOOSE: ").strip()
            if category not in self.categories:
                print("HUH.")
                continue
            self.ask_questions(category)
            if input("\WANNA PLAY AGAIN? (yes/no): ").strip().lower() != 'yes':
                break

        print(f"SCORE: {self.score}")
        self.save_score()
        print("TY BYE!")

    def ask_questions(self, category):
        category_questions = self.categories[category]
        random.shuffle(category_questions)

        for question in category_questions:
            print(f"\n{question['question']}")

            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")

            start_time = time.time()
            answer = input("UR ANS (number): ").strip()
            end_time = time.time()

            if end_time - start_time > 10:
                print("TIME'S UP!")
                continue

            if answer.isdigit() and int(answer) - 1 == question['answer']:
                print("YEE!")
                self.score += 1
            else:
                print(f"WRONGG!! CORRECT ANS: {question['options'][question['answer']]}")

        print(f"YOUR SCOREE: {self.score}")

    def save_score(self):
        name = input("user??: ").strip()
        self.leaderboard.append({"name": name, "score": self.score})
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x["score"], reverse=True)
        print("\nLEADERBOARD:")
        for rank, entry in enumerate(self.leaderboard, start=1):
            print(f"{rank}. {entry['name']} - {entry['score']}")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start()
