from pyscript import document

# Class Database
classes = {
    # Offense Classes
    "Scout": ("Offense","Scattergun","Pistol","Bat", "Scout.jpg", 
              "Fast but fragile; pick your battles, capture points fast, and use your speed to put out more damage with less risk."),
    "Soldier": ("Offense","Rocket Launcher","Shotgun","Shovel","Soldier.jpg",
                "High damage and health, rocket jump for mobility at the cost of health and deal high splash damage." ),
    "Pyro": ("Offense","Flamethrower","Flare Gun","Fire Axe","Pyro.jpg",
             "Close-range chaos; take flank routes to burn enemies, or airblast projectiles away from your teammates."),
    # Defense Classes
    "Demoman": ("Defense","Grenade Launcher","Stickybomb Launcher","Bottle","Demoman.jpg",
                "High splash and melee damage; set up stickies and bomb enemies, or pick heads with a sword and shield."),
    "Heavy": ("Defense","Minigun","Sandvich","Fists","Heavy.jpg",
              "High health but low mobility; gun down the enemy team with your minigun, and lead your team to the payload."),
    "Engineer": ("Defense","Shotgun","Pistol","Wrench","Engineer.jpg",
                 "Set up your buildings before they arrive; Defend your team with healing support, quick teleports, and sustained firepower."),
    # Support Classes
    "Medic": ("Support","Syringe Gun","Medi Gun","Bonesaw","Medic.jpg",
                "Heal your injured teammates, support the frontlines, and uber them to the point."),
    "Sniper": ("Support","Sniper Rifle","SMG","Kukri","Sniper.jpg",
               "Keep your battles far; pick off high-priorities with your snuper rifle and weaken their defenses."),
    "Spy": ("Support","Revolver","Sapper","Knife","Spy.jpg",
            "Disguise as the enemy, sneak into the backline, kill off high targets, and vanish before they notice.")
}

def element_checker(e):
    document.getElementById("result").innerHTML = ""

    class_name = document.getElementById("element_name").value.strip().title()

    result = classes.get(
        class_name,
        ("Class not found", "-", "-", "-","Blu.jpg")
    )
# Output
    document.getElementById("result").innerHTML = f"""
<div style="display:flex; align-items:center; justify-content:space-between; gap:20px;">
    <div style="flex:1;">
        <h4>{class_name}</h4><hr>
        <p><b>Class Type:</b> {result[0]}</p>
        <p><b>Primary:</b> {result[1]}</p>
        <p><b>Secondary:</b> {result[2]}</p>
        <p><b>Melee:</b> {result[3]}</p>
        <br>
        <br><p>{result[5]}</p>

    </div>
    <img src="{result[4]}"
         style="width:180px; height:auto;">

</div>
"""