from enum import IntEnum


class GameTag(IntEnum):
	IGNORE_DAMAGE = 1
	TAG_SCRIPT_DATA_NUM_1 = 2
	TAG_SCRIPT_DATA_NUM_2 = 3
	TAG_SCRIPT_DATA_ENT_1 = 4
	TAG_SCRIPT_DATA_ENT_2 = 5
	MISSION_EVENT = 6
	TIMEOUT = 7
	TURN_START = 8
	TURN_TIMER_SLUSH = 9
	PREMIUM = 12
	GOLD_REWARD_STATE = 13
	PLAYSTATE = 17
	LAST_AFFECTED_BY = 18
	STEP = 19
	TURN = 20
	FATIGUE = 22
	CURRENT_PLAYER = 23
	FIRST_PLAYER = 24
	RESOURCES_USED = 25
	RESOURCES = 26
	HERO_ENTITY = 27
	MAXHANDSIZE = 28
	STARTHANDSIZE = 29
	PLAYER_ID = 30
	TEAM_ID = 31
	TRIGGER_VISUAL = 32
	RECENTLY_ARRIVED = 33
	PROTECTED = 34
	PROTECTING = 35
	DEFENDING = 36
	PROPOSED_DEFENDER = 37
	ATTACKING = 38
	PROPOSED_ATTACKER = 39
	ATTACHED = 40
	EXHAUSTED = 43
	DAMAGE = 44
	HEALTH = 45
	ATK = 47
	COST = 48
	ZONE = 49
	CONTROLLER = 50
	OWNER = 51
	DEFINITION = 52
	ENTITY_ID = 53
	HISTORY_PROXY = 54
	COPY_DEATHRATTLE = 55
	COPY_DEATHRATTLE_INDEX = 56
	ELITE = 114
	MAXRESOURCES = 176
	CARD_SET = 183
	CARD_ID = 186
	DURABILITY = 187
	SILENCED = 188
	WINDFURY = 189
	TAUNT = 190
	STEALTH = 191
	SPELLPOWER = 192
	DIVINE_SHIELD = 194
	CHARGE = 197
	NEXT_STEP = 198
	CLASS = 199
	CARDRACE = 200
	FACTION = 201
	CARDTYPE = 202
	RARITY = 203
	STATE = 204
	SUMMONED = 205
	FREEZE = 208
	ENRAGED = 212
	OVERLOAD = 215
	LOYALTY = 216
	DEATHRATTLE = 217
	BATTLECRY = 218
	SECRET = 219
	COMBO = 220
	CANT_HEAL = 221
	CANT_DAMAGE = 222
	CANT_SET_ASIDE = 223
	CANT_REMOVE_FROM_GAME = 224
	CANT_READY = 225
	CANT_EXHAUST = 226
	CANT_ATTACK = 227
	CANT_TARGET = 228
	CANT_DESTROY = 229
	CANT_DISCARD = 230
	CANT_PLAY = 231
	CANT_DRAW = 232
	INCOMING_HEALING_MULTIPLIER = 233
	INCOMING_HEALING_ADJUSTMENT = 234
	INCOMING_HEALING_CAP = 235
	INCOMING_DAMAGE_MULTIPLIER = 236
	INCOMING_DAMAGE_ADJUSTMENT = 237
	INCOMING_DAMAGE_CAP = 238
	CANT_BE_HEALED = 239
	CANT_BE_DAMAGED = 240
	CANT_BE_SET_ASIDE = 241
	CANT_BE_REMOVED_FROM_GAME = 242
	CANT_BE_READIED = 243
	CANT_BE_EXHAUSTED = 244
	CANT_BE_ATTACKED = 245
	CANT_BE_TARGETED = 246
	CANT_BE_DESTROYED = 247
	CANT_BE_SUMMONING_SICK = 253
	FROZEN = 260
	JUST_PLAYED = 261
	LINKEDCARD = 262
	ZONE_POSITION = 263
	CANT_BE_FROZEN = 264
	COMBO_ACTIVE = 266
	CARD_TARGET = 267
	NUM_CARDS_PLAYED_THIS_TURN = 269
	CANT_BE_TARGETED_BY_OPPONENTS = 270
	NUM_TURNS_IN_PLAY = 271
	NUM_TURNS_LEFT = 272
	OUTGOING_DAMAGE_CAP = 273
	OUTGOING_DAMAGE_ADJUSTMENT = 274
	OUTGOING_DAMAGE_MULTIPLIER = 275
	OUTGOING_HEALING_CAP = 276
	OUTGOING_HEALING_ADJUSTMENT = 277
	OUTGOING_HEALING_MULTIPLIER = 278
	INCOMING_ABILITY_DAMAGE_ADJUSTMENT = 279
	INCOMING_COMBAT_DAMAGE_ADJUSTMENT = 280
	OUTGOING_ABILITY_DAMAGE_ADJUSTMENT = 281
	OUTGOING_COMBAT_DAMAGE_ADJUSTMENT = 282
	OUTGOING_ABILITY_DAMAGE_MULTIPLIER = 283
	OUTGOING_ABILITY_DAMAGE_CAP = 284
	INCOMING_ABILITY_DAMAGE_MULTIPLIER = 285
	INCOMING_ABILITY_DAMAGE_CAP = 286
	OUTGOING_COMBAT_DAMAGE_MULTIPLIER = 287
	OUTGOING_COMBAT_DAMAGE_CAP = 288
	INCOMING_COMBAT_DAMAGE_MULTIPLIER = 289
	INCOMING_COMBAT_DAMAGE_CAP = 290
	CURRENT_SPELLPOWER = 291
	ARMOR = 292
	MORPH = 293
	IS_MORPHED = 294
	TEMP_RESOURCES = 295
	OVERLOAD_OWED = 296
	NUM_ATTACKS_THIS_TURN = 297
	NEXT_ALLY_BUFF = 302
	MAGNET = 303
	FIRST_CARD_PLAYED_THIS_TURN = 304
	MULLIGAN_STATE = 305
	TAUNT_READY = 306
	STEALTH_READY = 307
	CHARGE_READY = 308
	CANT_BE_TARGETED_BY_ABILITIES = 311
	SHOULDEXITCOMBAT = 312
	CREATOR = 313
	CANT_BE_DISPELLED = 314
	PARENT_CARD = 316
	NUM_MINIONS_PLAYED_THIS_TURN = 317
	PREDAMAGE = 318
	ENCHANTMENT_BIRTH_VISUAL = 330
	ENCHANTMENT_IDLE_VISUAL = 331
	CANT_BE_TARGETED_BY_HERO_POWERS = 332
	HEALTH_MINIMUM = 337
	TAG_ONE_TURN_EFFECT = 338
	SILENCE = 339
	COUNTER = 340
	HAND_REVEALED = 348
	ADJACENT_BUFF = 350
	FORCED_PLAY = 352
	LOW_HEALTH_THRESHOLD = 353
	IGNORE_DAMAGE_OFF = 354
	SPELLPOWER_DOUBLE = 356
	HEALING_DOUBLE = 357
	NUM_OPTIONS_PLAYED_THIS_TURN = 358
	NUM_OPTIONS = 359
	TO_BE_DESTROYED = 360
	AURA = 362
	POISONOUS = 363
	HERO_POWER_DOUBLE = 366
	AI_MUST_PLAY = 367
	NUM_MINIONS_PLAYER_KILLED_THIS_TURN = 368
	NUM_MINIONS_KILLED_THIS_TURN = 369
	AFFECTED_BY_SPELL_POWER = 370
	EXTRA_DEATHRATTLES = 371
	START_WITH_1_HEALTH = 372
	IMMUNE_WHILE_ATTACKING = 373
	MULTIPLY_HERO_DAMAGE = 374
	MULTIPLY_BUFF_VALUE = 375
	CUSTOM_KEYWORD_EFFECT = 376
	TOPDECK = 377
	CANT_BE_TARGETED_BY_BATTLECRIES = 379
	SHOWN_HERO_POWER = 380
	DEATHRATTLE_RETURN_ZONE = 382
	STEADY_SHOT_CAN_TARGET = 383
	DISPLAYED_CREATOR = 385
	POWERED_UP = 386
	SPARE_PART = 388
	FORGETFUL = 389
	CAN_SUMMON_MAXPLUSONE_MINION = 390
	OBFUSCATED = 391
	BURNING = 392
	OVERLOAD_LOCKED = 393
	NUM_TIMES_HERO_POWER_USED_THIS_GAME = 394
	CURRENT_HEROPOWER_DAMAGE_BONUS = 395
	HEROPOWER_DAMAGE = 396
	LAST_CARD_PLAYED = 397
	NUM_FRIENDLY_MINIONS_THAT_DIED_THIS_TURN = 398
	NUM_CARDS_DRAWN_THIS_TURN = 399
	AI_ONE_SHOT_KILL = 400
	EVIL_GLOW = 401
	HIDE_COST = 402
	INSPIRE = 403
	RECEIVES_DOUBLE_SPELLDAMAGE_BONUS = 404
	HEROPOWER_ADDITIONAL_ACTIVATIONS = 405
	HEROPOWER_ACTIVATIONS_THIS_TURN = 406
	REVEALED = 410
	NUM_FRIENDLY_MINIONS_THAT_DIED_THIS_GAME = 412
	CANNOT_ATTACK_HEROES = 413
	LOCK_AND_LOAD = 414
	TREASURE = 415
	SHADOWFORM = 416
	NUM_FRIENDLY_MINIONS_THAT_ATTACKED_THIS_TURN = 417
	NUM_RESOURCES_SPENT_THIS_GAME = 418
	CHOOSE_BOTH = 419
	ELECTRIC_CHARGE_LEVEL = 420
	HEAVILY_ARMORED = 421
	DONT_SHOW_IMMUNE = 422
	HISTORY_PROXY_NO_BIG_CARD = 427

	# Only in card definitions
	Collectible = 321
	InvisibleDeathrattle = 335
	OneTurnEffect = 338
	ImmuneToSpellpower = 349
	AttackVisualType = 251
	DevState = 268
	GrantCharge = 355
	HealTarget = 361

	# strings
	CARDTEXT_INHAND = 184
	CARDNAME = 185
	CardTextInPlay = 252
	TARGETING_ARROW_TEXT = 325
	ARTISTNAME = 342
	LocalizationNotes = 344
	FLAVORTEXT = 351
	HOW_TO_EARN = 364
	HOW_TO_EARN_GOLDEN = 365

	# Renamed
	DEATH_RATTLE = DEATHRATTLE
	DEATHRATTLE_SENDS_BACK_TO_DECK = DEATHRATTLE_RETURN_ZONE
	RECALL = OVERLOAD
	RECALL_OWED = OVERLOAD_OWED
	TAG_HERO_POWER_DOUBLE = HERO_POWER_DOUBLE
	TAG_AI_MUST_PLAY = AI_MUST_PLAY
	OVERKILL = 380

	# Deleted
	DIVINE_SHIELD_READY = 314

	# Missing, only present in logs
	WEAPON = 334


TAG_NAMES = {
	GameTag.TRIGGER_VISUAL: "TriggerVisual",
	GameTag.HEALTH: "Health",
	GameTag.ATK: "Atk",
	GameTag.COST: "Cost",
	GameTag.ELITE: "Elite",
	GameTag.CARD_SET: "CardSet",
	GameTag.CARDTEXT_INHAND: "CardTextInHand",
	GameTag.CARDNAME: "CardName",
	GameTag.DURABILITY: "Durability",
	GameTag.WINDFURY: "Windfury",
	GameTag.TAUNT: "Taunt",
	GameTag.STEALTH: "Stealth",
	GameTag.SPELLPOWER: "Spellpower",
	GameTag.DIVINE_SHIELD: "Divine Shield",
	GameTag.CHARGE: "Charge",
	GameTag.CLASS: "Class",
	GameTag.CARDRACE: "Race",
	GameTag.FACTION: "Faction",
	GameTag.RARITY: "Rarity",
	GameTag.CARDTYPE: "CardType",
	GameTag.FREEZE: "Freeze",
	GameTag.ENRAGED: "Enrage",
	GameTag.RECALL: "Recall",
	GameTag.DEATHRATTLE: "Deathrattle",
	GameTag.BATTLECRY: "Battlecry",
	GameTag.SECRET: "Secret",
	GameTag.COMBO: "Combo",
	GameTag.CANT_BE_DAMAGED: "Cant Be Damaged",
	GameTag.AttackVisualType: "AttackVisualType",
	GameTag.CardTextInPlay: "CardTextInPlay",
	GameTag.DevState: "DevState",
	GameTag.MORPH: "Morph",
	GameTag.Collectible: "Collectible",
	GameTag.TARGETING_ARROW_TEXT: "TargetingArrowText",
	GameTag.ENCHANTMENT_BIRTH_VISUAL: "EnchantmentBirthVisual",
	GameTag.ENCHANTMENT_IDLE_VISUAL: "EnchantmentIdleVisual",
	GameTag.InvisibleDeathrattle: "InvisibleDeathrattle",
	GameTag.TAG_ONE_TURN_EFFECT: "OneTurnEffect",
	GameTag.SILENCE: "Silence",
	GameTag.COUNTER: "Counter",
	GameTag.ARTISTNAME: "ArtistName",
	GameTag.ImmuneToSpellpower: "ImmuneToSpellpower",
	GameTag.ADJACENT_BUFF: "AdjacentBuff",
	GameTag.FLAVORTEXT: "FlavorText",
	GameTag.HealTarget: "HealTarget",
	GameTag.AURA: "Aura",
	GameTag.POISONOUS: "Poisonous",
	GameTag.HOW_TO_EARN: "HowToGetThisCard",
	GameTag.HOW_TO_EARN_GOLDEN: "HowToGetThisGoldCard",
	GameTag.AI_MUST_PLAY: "AIMustPlay",
	GameTag.AFFECTED_BY_SPELL_POWER: "AffectedBySpellPower",
	GameTag.SPARE_PART: "SparePart",
}


##
# Card enums

class CardClass(IntEnum):
	INVALID = 0
	DEATHKNIGHT = 1
	DRUID = 2
	HUNTER = 3
	MAGE = 4
	PALADIN = 5
	PRIEST = 6
	ROGUE = 7
	SHAMAN = 8
	WARLOCK = 9
	WARRIOR = 10
	DREAM = 11
	COUNT = 12

	# alias
	NEUTRAL = INVALID


class CardSet(IntEnum):
	INVALID = 0
	TEST_TEMPORARY = 1
	CORE = 2
	EXPERT1 = 3
	REWARD = 4
	MISSIONS = 5
	DEMO = 6
	NONE = 7
	CHEAT = 8
	BLANK = 9
	DEBUG_SP = 10
	PROMO = 11
	NAXX = 12
	GVG = 13
	BRM = 14
	TGT = 15
	CREDITS = 16
	HERO_SKINS = 17
	TB = 18
	SLUSH = 19
	LOE = 20

	# Aliased from the original enums
	FP1 = 12
	PE1 = 13

	# Renamed
	FP2 = BRM
	PE2 = TGT

	@property
	def craftable(self):
		return self in (
			CardSet.EXPERT1,
			CardSet.GVG,
			CardSet.TGT,
		)


class CardType(IntEnum):
	INVALID = 0
	GAME = 1
	PLAYER = 2
	HERO = 3
	MINION = 4
	SPELL = 5
	ENCHANTMENT = 6
	WEAPON = 7
	ITEM = 8
	TOKEN = 9
	HERO_POWER = 10

	# Renamed
	ABILITY = SPELL

	@property
	def craftable(self):
		return self in (
			CardType.MINION,
			CardType.SPELL,
			CardType.WEAPON,
		)


class EnchantmentVisual(IntEnum):
	INVALID = 0
	POSITIVE = 1
	NEGATIVE = 2
	NEUTRAL = 3


class Faction(IntEnum):
	INVALID = 0
	HORDE = 1
	ALLIANCE = 2
	NEUTRAL = 3


class PlayReq(IntEnum):
	REQ_MINION_TARGET = 1
	REQ_FRIENDLY_TARGET = 2
	REQ_ENEMY_TARGET = 3
	REQ_DAMAGED_TARGET = 4
	REQ_ENCHANTED_TARGET = 5
	REQ_FROZEN_TARGET = 6
	REQ_CHARGE_TARGET = 7
	REQ_TARGET_MAX_ATTACK = 8
	REQ_NONSELF_TARGET = 9
	REQ_TARGET_WITH_RACE = 10
	REQ_TARGET_TO_PLAY = 11
	REQ_NUM_MINION_SLOTS = 12
	REQ_WEAPON_EQUIPPED = 13
	REQ_ENOUGH_MANA = 14
	REQ_YOUR_TURN = 15
	REQ_NONSTEALTH_ENEMY_TARGET = 16
	REQ_HERO_TARGET = 17
	REQ_SECRET_CAP = 18
	REQ_MINION_CAP_IF_TARGET_AVAILABLE = 19
	REQ_MINION_CAP = 20
	REQ_TARGET_ATTACKED_THIS_TURN = 21
	REQ_TARGET_IF_AVAILABLE = 22
	REQ_MINIMUM_ENEMY_MINIONS = 23
	REQ_TARGET_FOR_COMBO = 24
	REQ_NOT_EXHAUSTED_ACTIVATE = 25
	REQ_UNIQUE_SECRET = 26
	REQ_TARGET_TAUNTER = 27
	REQ_CAN_BE_ATTACKED = 28
	REQ_ACTION_PWR_IS_MASTER_PWR = 29
	REQ_TARGET_MAGNET = 30
	REQ_ATTACK_GREATER_THAN_0 = 31
	REQ_ATTACKER_NOT_FROZEN = 32
	REQ_HERO_OR_MINION_TARGET = 33
	REQ_CAN_BE_TARGETED_BY_SPELLS = 34
	REQ_SUBCARD_IS_PLAYABLE = 35
	REQ_TARGET_FOR_NO_COMBO = 36
	REQ_NOT_MINION_JUST_PLAYED = 37
	REQ_NOT_EXHAUSTED_HERO_POWER = 38
	REQ_CAN_BE_TARGETED_BY_OPPONENTS = 39
	REQ_ATTACKER_CAN_ATTACK = 40
	REQ_TARGET_MIN_ATTACK = 41
	REQ_CAN_BE_TARGETED_BY_HERO_POWERS = 42
	REQ_ENEMY_TARGET_NOT_IMMUNE = 43
	REQ_ENTIRE_ENTOURAGE_NOT_IN_PLAY = 44
	REQ_MINIMUM_TOTAL_MINIONS = 45
	REQ_MUST_TARGET_TAUNTER = 46
	REQ_UNDAMAGED_TARGET = 47
	REQ_CAN_BE_TARGETED_BY_BATTLECRIES = 48
	REQ_STEADY_SHOT = 49
	REQ_MINION_OR_ENEMY_HERO = 50
	REQ_TARGET_IF_AVAILABLE_AND_DRAGON_IN_HAND = 51
	REQ_LEGENDARY_TARGET = 52
	REQ_FRIENDLY_MINION_DIED_THIS_TURN = 53
	REQ_FRIENDLY_MINION_DIED_THIS_GAME = 54
	REQ_ENEMY_WEAPON_EQUIPPED = 55
	REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_MINIONS = 56
	REQ_TARGET_WITH_BATTLECRY = 57
	REQ_TARGET_WITH_DEATHRATTLE = 58
	REQ_DRAG_TO_PLAY = 59


class Race(IntEnum):
	INVALID = 0
	BLOODELF = 1
	DRAENEI = 2
	DWARF = 3
	GNOME = 4
	GOBLIN = 5
	HUMAN = 6
	NIGHTELF = 7
	ORC = 8
	TAUREN = 9
	TROLL = 10
	UNDEAD = 11
	WORGEN = 12
	GOBLIN2 = 13
	MURLOC = 14
	DEMON = 15
	SCOURGE = 16
	MECHANICAL = 17
	ELEMENTAL = 18
	OGRE = 19
	BEAST = 20
	TOTEM = 21
	NERUBIAN = 22
	PIRATE = 23
	DRAGON = 24

	# Aliased
	PET = 20


class Rarity(IntEnum):
	INVALID = 0
	COMMON = 1
	FREE = 2
	RARE = 3
	EPIC = 4
	LEGENDARY = 5

	# TB_BlingBrawl_Blade1e (10956)
	UNKNOWN_6 = 6

	@property
	def craftable(self):
		return self in (
			Rarity.COMMON,
			Rarity.RARE,
			Rarity.EPIC,
			Rarity.LEGENDARY,
		)

	@property
	def crafting_costs(self):
		return CRAFTING_COSTS.get(self, (0, 0))

	@property
	def disenchant_costs(self):
		return DISENCHANT_COSTS.get(self, (0, 0))


CRAFTING_COSTS = {
	Rarity.COMMON: (40, 400),
	Rarity.RARE: (100, 800),
	Rarity.EPIC: (400, 1600),
	Rarity.LEGENDARY: (1600, 3200),
}

DISENCHANT_COSTS = {
	Rarity.COMMON: (5, 50),
	Rarity.RARE: (20, 100),
	Rarity.EPIC: (100, 400),
	Rarity.LEGENDARY: (400, 1600),
}


class Zone(IntEnum):
	INVALID = 0
	PLAY = 1
	DECK = 2
	HAND = 3
	GRAVEYARD = 4
	REMOVEDFROMGAME = 5
	SETASIDE = 6
	SECRET = 7

	# Not public
	DISCARD = -2


##
# Game enums

class ChoiceType(IntEnum):
	INVALID = 0
	MULLIGAN = 1
	GENERAL = 2


class GameType(IntEnum):
	GT_UNKNOWN = 0
	GT_VS_AI = 1
	GT_VS_FRIEND = 2
	GT_TUTORIAL = 4
	GT_ARENA = 5
	GT_TEST = 6
	GT_RANKED = 7
	GT_UNRANKED = 8
	GT_TAVERNBRAWL = 16
	GT_TB_2P_COOP = 18
	GT_LAST = 17


class GoldRewardState(IntEnum):
	INVALID = 0
	ELIGIBLE = 1
	WRONG_GAME_TYPE = 2
	ALREADY_CAPPED = 3
	BAD_RATING = 4
	SHORT_GAME = 5
	OVER_CAIS = 6


class MetaDataType(IntEnum):
	# From HistoryMeta.Type
	TARGET = 0
	DAMAGE = 1
	HEALING = 2
	JOUST = 3

	# Renamed in 9786 from PowerHistoryMetaData.Type
	META_TARGET = TARGET
	META_DAMAGE = DAMAGE
	META_HEALING = HEALING


class Mulligan(IntEnum):
	INVALID = 0
	INPUT = 1
	DEALING = 2
	WAITING = 3
	DONE = 4


class OptionType(IntEnum):
	PASS = 1
	END_TURN = 2
	POWER = 3


class PlayState(IntEnum):
	INVALID = 0
	PLAYING = 1
	WINNING = 2
	LOSING = 3
	WON = 4
	LOST = 5
	TIED = 6
	DISCONNECTED = 7
	CONCEDED = 8

	# Renamed in 10833
	QUIT = CONCEDED


class PowType(IntEnum):
	FULL_ENTITY = 1
	SHOW_ENTITY = 2
	HIDE_ENTITY = 3
	TAG_CHANGE = 4
	ACTION_START = 5
	ACTION_END = 6
	CREATE_GAME = 7
	META_DATA = 8


class PowSubType(IntEnum):
	ATTACK = 1
	JOUST = 2
	POWER = 3
	TRIGGER = 5
	DEATHS = 6
	PLAY = 7
	FATIGUE = 8

	# Removed
	SCRIPT = 4
	ACTION = 99

	# Renamed
	CONTINUOUS = 2


class State(IntEnum):
	INVALID = 0
	LOADING = 1
	RUNNING = 2
	COMPLETE = 3


class Step(IntEnum):
	INVALID = 0
	BEGIN_FIRST = 1
	BEGIN_SHUFFLE = 2
	BEGIN_DRAW = 3
	BEGIN_MULLIGAN = 4
	MAIN_BEGIN = 5
	MAIN_READY = 6
	MAIN_RESOURCE = 7
	MAIN_DRAW = 8
	MAIN_START = 9
	MAIN_ACTION = 10
	MAIN_COMBAT = 11
	MAIN_END = 12
	MAIN_NEXT = 13
	FINAL_WRAPUP = 14
	FINAL_GAMEOVER = 15
	MAIN_CLEANUP = 16
	MAIN_START_TRIGGERS = 17


##
# Misc

class Booster(IntEnum):
	INVALID = 0
	CLASSIC = 1
	GOBLINS_VS_GNOMES = 9
	THE_GRAND_TOURNAMENT = 10


class Type(IntEnum):
	UNKNOWN = 0
	BOOL = 1
	NUMBER = 2
	COUNTER = 3
	ENTITY = 4
	PLAYER = 5
	TEAM = 6
	ENTITY_DEFINITION = 7
	STRING = 8

	# Not present at the time
	LOCSTRING = -2


TAG_TYPES = {
	GameTag.TRIGGER_VISUAL: Type.BOOL,
	GameTag.ELITE: Type.BOOL,
	GameTag.CARD_SET: CardSet,
	GameTag.CARDTEXT_INHAND: Type.LOCSTRING,
	GameTag.CARDNAME: Type.LOCSTRING,
	GameTag.WINDFURY: Type.BOOL,
	GameTag.TAUNT: Type.BOOL,
	GameTag.STEALTH: Type.BOOL,
	GameTag.SPELLPOWER: Type.BOOL,
	GameTag.DIVINE_SHIELD: Type.BOOL,
	GameTag.CHARGE: Type.BOOL,
	GameTag.CLASS: CardClass,
	GameTag.CARDRACE: Race,
	GameTag.FACTION: Faction,
	GameTag.RARITY: Rarity,
	GameTag.CARDTYPE: CardType,
	GameTag.FREEZE: Type.BOOL,
	GameTag.ENRAGED: Type.BOOL,
	GameTag.DEATHRATTLE: Type.BOOL,
	GameTag.BATTLECRY: Type.BOOL,
	GameTag.SECRET: Type.BOOL,
	GameTag.COMBO: Type.BOOL,
	GameTag.CANT_BE_DAMAGED: Type.BOOL,
	# GameTag.AttackVisualType: AttackVisualType,
	GameTag.CardTextInPlay: Type.LOCSTRING,
	# GameTag.DevState: DevState,
	GameTag.MORPH: Type.BOOL,
	GameTag.Collectible: Type.BOOL,
	GameTag.TARGETING_ARROW_TEXT: Type.LOCSTRING,
	GameTag.ENCHANTMENT_BIRTH_VISUAL: EnchantmentVisual,
	GameTag.ENCHANTMENT_IDLE_VISUAL: EnchantmentVisual,
	GameTag.InvisibleDeathrattle: Type.BOOL,
	GameTag.TAG_ONE_TURN_EFFECT: Type.BOOL,
	GameTag.SILENCE: Type.BOOL,
	GameTag.COUNTER: Type.BOOL,
	GameTag.ARTISTNAME: Type.LOCSTRING,
	GameTag.ImmuneToSpellpower: Type.BOOL,
	GameTag.ADJACENT_BUFF: Type.BOOL,
	GameTag.FLAVORTEXT: Type.BOOL,
	GameTag.HealTarget: Type.BOOL,
	GameTag.AURA: Type.BOOL,
	GameTag.POISONOUS: Type.BOOL,
	GameTag.HOW_TO_EARN: Type.LOCSTRING,
	GameTag.HOW_TO_EARN_GOLDEN: Type.LOCSTRING,
	GameTag.AI_MUST_PLAY: Type.BOOL,
	GameTag.AFFECTED_BY_SPELL_POWER: Type.BOOL,
	GameTag.SPARE_PART: Type.BOOL,
	GameTag.PLAYSTATE: PlayState,
	GameTag.ZONE: Zone,
	GameTag.STEP: Step,
	GameTag.NEXT_STEP: Step,
	GameTag.STATE: State,
	GameTag.MULLIGAN_STATE: Mulligan,
}


LOCALIZED_TAGS = [k for k, v in TAG_TYPES.items() if v == Type.LOCSTRING]


class Locale(IntEnum):
	UNKNOWN = -1
	enUS = 0
	enGB = 1
	frFR = 2
	deDE = 3
	koKR = 4
	esES = 5
	esMX = 6
	ruRU = 7
	zhTW = 8
	zhCN = 9
	itIT = 10
	ptBR = 11
	plPL = 12
	ptPT = 13
	jaJP = 14

	@property
	def unused(self):
		return self in (self.UNKNOWN, self.enGB, self.ptPT)


if __name__ == "__main__":
	import json

	print(json.dumps({
		k: dict(v.__members__) for k, v in globals().items() if (
			isinstance(v, type) and issubclass(v, IntEnum) and k != "IntEnum"
		)
	}))
