import tkinter as tk
import random
import time

# 🎨 Wood Style Color Palette
WOOD_BACKGROUND       = "#DEB887"
WOOD_BUTTON_COLOR     = "#D2B48C"
WOOD_ACTIVE_COLOR     = "#C2A684"
COMPLETED_COLOR       = "#C06236"
COMPLETED_TEXT_COLOR  = "#5D4037"
CORRECT_COLOR         = "#228B22"
INCORRECT_COLOR       = "#CD5C5C"
RESET_COLOR           = "#E0CDA9"
TEXT_COLOR            = "#3E2723"

# 🖋 Base Font (sizes will be scaled dynamically)
BASE_TITLE_SIZE    = 36
BASE_LABEL_SIZE    = 28
BASE_BUTTON_SIZE   = 18
BASE_QUESTION_SIZE = 48

# 🔬 List of elements: (Name, Symbol)
elements = [
    ('Hydrogen', 'H'), ('Helium', 'He'), ('Lithium', 'Li'), ('Beryllium', 'Be'),
    ('Boron', 'B'), ('Carbon', 'C'), ('Nitrogen', 'N'), ('Oxygen', 'O'),
    ('Fluorine', 'F'), ('Neon', 'Ne'), ('Sodium', 'Na'), ('Magnesium', 'Mg'),
    ('Aluminum', 'Al'), ('Silicon', 'Si'), ('Phosphorus', 'P'), ('Sulfur', 'S'),
    ('Chlorine', 'Cl'), ('Argon', 'Ar'), ('Potassium', 'K'), ('Calcium', 'Ca'),
    ('Scandium', 'Sc'), ('Titanium', 'Ti'), ('Vanadium', 'V'), ('Chromium', 'Cr'),
    ('Manganese', 'Mn'), ('Iron', 'Fe'), ('Cobalt', 'Co'), ('Nickel', 'Ni'),
    ('Copper', 'Cu'), ('Zinc', 'Zn'), ('Gallium', 'Ga'), ('Germanium', 'Ge'),
    ('Arsenic', 'As'), ('Selenium', 'Se'), ('Bromine', 'Br'), ('Krypton', 'Kr'),
    ('Rubidium', 'Rb'), ('Strontium', 'Sr'), ('Yttrium', 'Y'), ('Zirconium', 'Zr'),
    ('Niobium', 'Nb'), ('Molybdenum', 'Mo'), ('Technetium', 'Tc'), ('Ruthenium', 'Ru'),
    ('Rhodium', 'Rh'), ('Palladium', 'Pd'), ('Silver', 'Ag'), ('Cadmium', 'Cd'),
    ('Indium', 'In'), ('Tin', 'Sn'), ('Antimony', 'Sb'), ('Tellurium', 'Te'),
    ('Iodine', 'I'), ('Xenon', 'Xe'), ('Cesium', 'Cs'), ('Barium', 'Ba'),
    ('Lanthanum', 'La'), ('Cerium', 'Ce'), ('Praseodymium', 'Pr'), ('Neodymium', 'Nd'),
    ('Promethium', 'Pm'), ('Samarium', 'Sm'), ('Europium', 'Eu'), ('Gadolinium', 'Gd'),
    ('Terbium', 'Tb'), ('Dysprosium', 'Dy'), ('Holmium', 'Ho'), ('Erbium', 'Er'),
    ('Thulium', 'Tm'), ('Ytterbium', 'Yb'), ('Lutetium', 'Lu'), ('Hafnium', 'Hf'),
    ('Tantalum', 'Ta'), ('Tungsten', 'W'), ('Rhenium', 'Re'), ('Osmium', 'Os'),
    ('Iridium', 'Ir'), ('Platinum', 'Pt'), ('Gold', 'Au'), ('Mercury', 'Hg'),
    ('Thallium', 'Tl'), ('Lead', 'Pb'), ('Bismuth', 'Bi'), ('Polonium', 'Po'),
    ('Astatine', 'At'), ('Radon', 'Rn'), ('Francium', 'Fr'), ('Radium', 'Ra'),
    ('Actinium', 'Ac'), ('Thorium', 'Th'), ('Protactinium', 'Pa'), ('Uranium', 'U'),
    ('Neptunium', 'Np'), ('Plutonium', 'Pu'), ('Americium', 'Am'), ('Curium', 'Cm'),
    ('Berkelium', 'Bk'), ('Californium', 'Cf'), ('Einsteinium', 'Es'), ('Fermium', 'Fm'),
    ('Mendelevium', 'Md'), ('Nobelium', 'No'), ('Lawrencium', 'Lr')
]

# 📐 Positions of the elements in the table (row, column)
element_positions = {
    'H': (0, 0), 'He': (0, 17),
    'Li': (1, 0), 'Be': (1, 1), 'B': (1, 12), 'C': (1, 13), 'N': (1, 14),
    'O': (1, 15), 'F': (1, 16), 'Ne': (1, 17),
    'Na': (2, 0), 'Mg': (2, 1), 'Al': (2, 12), 'Si': (2, 13), 'P': (2, 14),
    'S': (2, 15), 'Cl': (2, 16), 'Ar': (2, 17),
    'K': (3, 0), 'Ca': (3, 1), 'Sc': (3, 2), 'Ti': (3, 3), 'V': (3, 4),
    'Cr': (3, 5), 'Mn': (3, 6), 'Fe': (3, 7), 'Co': (3, 8), 'Ni': (3, 9),
    'Cu': (3, 10), 'Zn': (3, 11), 'Ga': (3, 12), 'Ge': (3, 13), 'As': (3, 14),
    'Se': (3, 15), 'Br': (3, 16), 'Kr': (3, 17),
    'Rb': (4, 0), 'Sr': (4, 1), 'Y': (4, 2), 'Zr': (4, 3), 'Nb': (4, 4),
    'Mo': (4, 5), 'Tc': (4, 6), 'Ru': (4, 7), 'Rh': (4, 8), 'Pd': (4, 9),
    'Ag': (4, 10), 'Cd': (4, 11), 'In': (4, 12), 'Sn': (4, 13), 'Sb': (4, 14),
    'Te': (4, 15), 'I': (4, 16), 'Xe': (4, 17),
    'Cs': (5, 0), 'Ba': (5, 1),
    'La': (5, 2), 'Hf': (5, 3), 'Ta': (5, 4), 'W': (5, 5), 'Re': (5, 6),
    'Os': (5, 7), 'Ir': (5, 8), 'Pt': (5, 9), 'Au': (5, 10), 'Hg': (5, 11),
    'Tl': (5, 12), 'Pb': (5, 13), 'Bi': (5, 14), 'Po': (5, 15), 'At': (5, 16), 'Rn': (5, 17),
    'Fr': (6, 0), 'Ra': (6, 1),
    'Ac': (6, 2),
    # Lanthanides and Actinides
    'Th': (8, 4), 'Pa': (8, 5), 'U': (8, 6), 'Np': (8, 7),
    'Pu': (8, 8), 'Am': (8, 9), 'Cm': (8, 10), 'Bk': (8, 11), 'Cf': (8, 12),
    'Es': (8, 13), 'Fm': (8, 14), 'Md': (8, 15), 'No': (8, 16), 'Lr': (8, 17),
    'Ce': (7, 4), 'Pr': (7, 5), 'Nd': (7, 6), 'Pm': (7, 7), 'Sm': (7, 8),
    'Eu': (7, 9), 'Gd': (7, 10), 'Tb': (7, 11), 'Dy': (7, 12), 'Ho': (7, 13),
    'Er': (7, 14), 'Tm': (7, 15), 'Yb': (7, 16), 'Lu': (7, 17)
}

# Helper map: from element name to symbol
name_to_symbol = {name: symbol for name, symbol in elements if symbol in element_positions}

# 🎮 Game state variables
current_element     = None
score               = 0
total_questions     = 0
next_question_ready = False
game_started        = False
start_time          = 0
elapsed_time        = 0
completed_elements  = set()   # names of elements already used
last_answered       = None      # last element answered

# Global variable for debouncing resize
resize_after_id = None

def format_time(total_seconds):
    total_seconds = int(total_seconds)
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours   = (total_seconds // 3600) % 1000
    return f"{hours:03d}:{minutes:02d}:{seconds:02d}"

def start_timer():
    global start_time
    start_time = time.perf_counter()

def update_timer():
    if game_started and not next_question_ready:
        elapsed = elapsed_time + (time.perf_counter() - start_time) * 60
        timer_label.config(text=f"Time: {format_time(elapsed)}")
    root.after(10, update_timer)

def on_element_click(element_name, button):
    global score, total_questions, next_question_ready, elapsed_time, last_answered, start_time
    if game_started and not next_question_ready:
        total_questions += 1
        if element_name == current_element:
            score += 1
            button.config(bg=CORRECT_COLOR, activebackground=CORRECT_COLOR)
        else:
            button.config(bg=INCORRECT_COLOR, activebackground=INCORRECT_COLOR)
            correct_button = button_map[current_element]
            correct_button.config(bg=CORRECT_COLOR, activebackground=CORRECT_COLOR)
        update_score_label()
        completed_elements.add(current_element)
        last_answered = current_element
        next_question_ready = True
        elapsed_time += (time.perf_counter() - start_time) * 60

def reset_button_colors():
    for name, button in button_map.items():
        if name not in completed_elements:
            button.config(bg=WOOD_BUTTON_COLOR, fg=TEXT_COLOR, activebackground=WOOD_ACTIVE_COLOR)

def next_question():
    global current_element, game_started
    available = [(name, symbol) for (name, symbol) in elements 
                 if name not in completed_elements and symbol in element_positions]
    if available:
        current_element, _ = random.choice(available)
        question_label.config(text=f"{current_element}")
    else:
        question_label.config(text="Quiz completed! Click Reset to restart.")
        game_started = False

def update_score_label():
    score_label.config(text=f"Score: {score}/{total_questions}")

def reset_game():
    global score, total_questions, next_question_ready, game_started
    global start_time, elapsed_time, current_element, completed_elements, last_answered
    score = 0
    total_questions = 0
    next_question_ready = False
    game_started = False
    start_time = 0
    elapsed_time = 0
    current_element = None
    completed_elements.clear()
    last_answered = None
    question_label.config(text="Right click to start")
    update_score_label()
    for name, button in button_map.items():
        button.config(bg=WOOD_BUTTON_COLOR, fg=TEXT_COLOR, state="normal", activebackground=WOOD_ACTIVE_COLOR)

def on_right_click(event):
    global next_question_ready, game_started, start_time, last_answered
    if not game_started:
        game_started = True
        next_question()
        start_timer()
    elif next_question_ready:
        if last_answered is not None:
            button_map[last_answered].config(bg=COMPLETED_COLOR, fg=COMPLETED_TEXT_COLOR,
                                             disabledforeground=COMPLETED_TEXT_COLOR, state="disabled")
            last_answered = None
        reset_button_colors()
        next_question()
        next_question_ready = False
        start_timer()

# ── Create the main window ──
root = tk.Tk()
root.title("Periodic Table Quiz")
root.configure(bg=WOOD_BACKGROUND)

# Set the window size to 1280x720 and center it on the screen
window_width = 1280
window_height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Top frame: header, reset button, timer, score and question label
top_frame = tk.Frame(root, bg=WOOD_BACKGROUND)
top_frame.pack(side="top", fill="x", pady=10)

header_frame = tk.Frame(top_frame, bg=WOOD_BACKGROUND)
header_frame.pack(pady=(0,10))

reset_button = tk.Button(header_frame, text="Reset", bg=RESET_COLOR, activebackground=RESET_COLOR,
                         fg=TEXT_COLOR, activeforeground=TEXT_COLOR, relief="flat", bd=0, padx=10, pady=5,
                         command=reset_game)
reset_button.pack(side="left", padx=(0, 20))

title_label = tk.Label(header_frame, text="Periodic Table Quiz", bg=WOOD_BACKGROUND, fg=TEXT_COLOR)
title_label.pack(side="left")

info_frame = tk.Frame(top_frame, bg=WOOD_BACKGROUND)
info_frame.pack()

timer_label = tk.Label(info_frame, text="Time: 000:00:00", bg=WOOD_BACKGROUND, fg=TEXT_COLOR, width=15)
timer_label.pack(side="left", padx=20)

score_label = tk.Label(info_frame, text="Score: 0/0", bg=WOOD_BACKGROUND, fg=TEXT_COLOR, width=15)
score_label.pack(side="left", padx=20)

# The question label always uses a large font to avoid later realignments.
question_label = tk.Label(top_frame, text="Right click to start", bg=WOOD_BACKGROUND, fg=TEXT_COLOR)
question_label.pack(pady=10)

# Frame for the periodic table grid
grid_frame = tk.Frame(root, bg=WOOD_BACKGROUND)
grid_frame.pack(side="top", fill="both", expand=True)

# Map for the buttons (key: element name)
button_map = {}

for name, symbol in elements:
    if symbol in element_positions:
        btn = tk.Button(grid_frame, text=symbol, bg=WOOD_BUTTON_COLOR, fg=TEXT_COLOR,
                        relief="ridge", bd=2, activebackground=WOOD_ACTIVE_COLOR)
        btn.config(command=lambda n=name, b=btn: on_element_click(n, b) if game_started else None)
        button_map[name] = btn

# ── Function to reposition and resize the grid buttons ──
def resize_buttons():
    width = grid_frame.winfo_width()
    height = grid_frame.winfo_height()
    btn_width = width / 18
    btn_height = height / 10
    for name, btn in button_map.items():
        symbol = name_to_symbol[name]
        if symbol in element_positions:
            row, col = element_positions[symbol]
            x_pos = col * btn_width
            y_pos = row * btn_height
            btn.place(x=x_pos, y=y_pos, width=btn_width, height=btn_height)

# ── Function to dynamically update font sizes ──
def update_fonts():
    # Calculate a scaling factor based on a reference window of 1000x600
    factor = min(root.winfo_width() / 1000, root.winfo_height() / 600)
    new_title_size    = max(8, int(BASE_TITLE_SIZE * factor))
    new_label_size    = max(8, int(BASE_LABEL_SIZE * factor))
    new_button_size   = max(8, int(BASE_BUTTON_SIZE * factor))
    new_question_size = max(8, int(BASE_QUESTION_SIZE * factor))
    
    title_label.config(font=("Georgia", new_title_size, "bold"))
    timer_label.config(font=("Georgia", new_label_size))
    score_label.config(font=("Georgia", new_label_size))
    question_label.config(font=("Georgia", new_question_size, "bold"))
    reset_button.config(font=("Georgia", new_button_size, "bold"))
    for btn in button_map.values():
        btn.config(font=("Georgia", new_button_size, "bold"))

# ── Debounced function for resizing ──
def on_resize(event=None):
    global resize_after_id
    if resize_after_id is not None:
        root.after_cancel(resize_after_id)
    resize_after_id = root.after(100, perform_resize)

def perform_resize():
    update_fonts()
    resize_buttons()
    global resize_after_id
    resize_after_id = None

# Binding the <Configure> event for window resizing with debouncing
root.bind("<Configure>", on_resize)

# Binding right click to handle starting and moving to the next question
root.bind("<Button-3>", on_right_click)

# Run an immediate layout update after the first rendering to ensure consistent positioning
root.after_idle(perform_resize)

update_timer()
root.mainloop()
