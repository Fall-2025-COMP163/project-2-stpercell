"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"{self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"{self.char2.name} wins!")
        else:
            print("It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================
class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """

    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name          # Character's name
        self.health = health      # Health points (HP)
        self.strength = strength  # Physical power for attacks
        self.magic = magic        # Magical ability (unused here, but for later)

    def attack(self, target):
        """
        Basic attack method that all characters can use.
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        """Reduce the character's health when attacked"""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} now has {self.health} health remaining.")

    def display_stats(self):
        #Show basic character stats
        print(f"{self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")
        """
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        """
        pass

      
class Player(Character):
       #STarts player char
    def __init__(self, name, character_class, health, strength, magic):
        # Call the parent to set up name, health, strength, and magic. STuff basically
        super().__init__(name, health, strength, magic)
        # Store the character's class Warrior, Mage, Rogue
        self.character_class = character_class
        # Add attributes
        self.level = 1
        self.experience = 0
        pass

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        bonus_damage = 5  # Extra physical damage
        total_damage = self.strength + bonus_damage
        print(f"{self.name} swings a mighty sword at {target.name} for {total_damage} damage!")
        target.take_damage(total_damage)
        pass
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength * 2  # Double damage
        print(f"{self.name} unleashes a POWER STRIKE on {target.name} for {damage} damage!! ⚔️")
        target.take_damage(damage)
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        pass

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        super().__init__(name, "Mage", health=70, strength=5, magic=20)
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        magic_damage = self.magic + 3  # Slight bonus magic damage
        print(f"{self.name} casts a magic bolt at {target.name} for {magic_damage} damage!")
        target.take_damage(magic_damage)
        pass
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        damage = self.magic * 2 + 5  # Big, flashy magical hit
        print(f"{self.name} hurls a FIREBALL at {target.name} for {damage} damage!!")
        target.take_damage(damage)
        pass

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)
        self.last_attack_was_crit = False  # Track crit alternation
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        # Alternate between normal and critical hits to avoid randomness
        if self.last_attack_was_crit:
            damage = self.strength
            print(f"{self.name} swiftly attacks {target.name} for {damage} damage.")
            self.last_attack_was_crit = False
        else:
            damage = self.strength * 2  # Critical hit = double damage
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!!")
            self.last_attack_was_crit = True
        
        target.take_damage(damage)
        pass
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        # TODO: Implement sneak attack
        # Should always do critical damage
        damage = self.strength * 2  # Always double damage
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!! 🕶️")
        target.take_damage(damage)
        pass

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # TODO: Store weapon name and damage bonus
        pass
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus
        pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
