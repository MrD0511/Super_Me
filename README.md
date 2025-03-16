# **Super Mario in Pygame**

A classic **Super Mario Bros.** remake built using **Pygame**. This project recreates the original gameplay experience, featuring Mario, Goombas, bricks, question blocks, coins, and a level-ending flagpole.

---

## **Features**
- 🎮 **Player Movement**: Move left, right, and jump.
- 🏃 **Smooth Animations**: Running, jumping, and idle animations for Mario.
- ⚙️ **Physics System**: Gravity, jumping, and collision handling.
- 👾 **Enemies**: Goombas that can be defeated by jumping on them.
- 💰 **Blocks & Coins**: Breakable blocks and question blocks that give coins.
- 🚩 **Flagpole Ending**: Reach the flag to complete the level with animations.
- 🔊 **Sound Effects**: Authentic Mario sounds for jumping, dying, and level completion.

---

## **Controls**
| Key | Action |
|------|--------|
| ← | Move Left |
| → | Move Right |
| Space / ↑ | Jump |

---

## **Installation & Setup**
### **Prerequisites**
- Python (>=3.7)
- Pygame (`pip install pygame`)

### **How to Run**
1. **Clone the Repository**
   ```sh
   git clone https://github.com/MrD0511/Super_Me.git
   cd super-mario-pygame

   ```
2. **Run the Game**
   ```sh
   py app.py
   ```
---

### **Project Structure**

```sh
│── assets/               # Images, sounds, and other assets
│── game_objects/         # All game objects like blocks, enemies, and flag
│── app.py                # Entry point of the game
│── player.py             # Player movement and interactions
│── goombas.py            # Enemy logic
│── ground_block.py       # Ground, bricks, and treasure blocks
│── flag.py               # Flagpole logic
|── mountain.py           # Logic for mountains
|── big_mountain.py
|── bush.py
|── camera.py             # Logic for camera movement
|── cloud.py
|── castle.py
|── tube.py
│── README.md             # Project documentation
```


### **Future Improvements**

- ✅ Add pipes and hidden areas
- ✅ Add more enemy types
- ✅ Implement power-ups (mushrooms, fireballs)
- ✅ Multiple levels with level selection


### **Credits**

- Game Development – Dhruv Sharma
- Assets – Original Super Mario Bros. sprites & sounds (used for educational purposes)
- Tools Used – Pygame, Python


### **License**

This project is for educational purposes only and is not intended for commercial use.
Super Mario Bros. is a trademark of Nintendo.

**🚀 Enjoy the game! Feel free to suggest any modifications. 😃**