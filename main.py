import time
import logging
import datetime
import csv
import os
#import pandas as pd


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from aiogram.utils.markdown import hide_link
from aiogram.utils.markdown import hlink


#База
TOKEN = "5942349292:AAGNee5edMXLdGl3huofXhp2gvLFBkBobpU"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot)


#Кнопки и клавиатура
button1_menu = KeyboardButton('Все страны')
button2_menu = KeyboardButton('Помощь')
button3_menu = KeyboardButton('Консультация специалиста')
buttons_menu = [[button1_menu, button2_menu], [button3_menu]]
keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_menu.add(*[button for button_row in buttons_menu for button in button_row])


button1_congo = KeyboardButton('Конго-Киншаса')
button2_congo = KeyboardButton('Конго-Браззавиль')
buttons_congo = [[button1_congo], [button2_congo]]
keyboard_congo = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_congo.add(*[button for button_row in buttons_congo for button in button_row])


button1_guinea = KeyboardButton('Гвинейская Республика')
button2_guinea = KeyboardButton('Гвинея-Бисау')
button3_guinea = KeyboardButton('Экваториальная Гвинея')
button4_guinea = KeyboardButton('Папуа-Новая Гвинея')
buttons_guinea = [[button1_guinea, button2_guinea], [button3_guinea, button4_guinea]]
keyboard_guinea = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_guinea.add(*[button for button_row in buttons_guinea for button in button_row])


button1_korea = KeyboardButton('Северная Корея')
button2_korea = KeyboardButton('Южная Корея')
buttons_korea = [[button1_korea], [button2_korea]]
keyboard_korea = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_korea.add(*[button for button_row in buttons_korea for button in button_row])


button1_samoa = KeyboardButton('Американское Самоа')
button2_samoa = KeyboardButton('Западное Самоа')
buttons_samoa = [[button1_samoa], [button2_samoa]]
keyboard_samoa = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_samoa.add(*[button for button_row in buttons_samoa for button in button_row])


button1_sudan = KeyboardButton('Республика Судан')
button2_sudan = KeyboardButton('Южный Судан')
buttons_sudan = [[button1_sudan], [button2_sudan]]
keyboard_sudan = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_sudan.add(*[button for button_row in buttons_sudan for button in button_row])


button1_virgin_islands = KeyboardButton('Американские Виргинские острова')
button2_virgin_islands = KeyboardButton('Британские Виргинские острова')
buttons_virgin_islands = [[button1_virgin_islands], [button2_virgin_islands]]
keyboard_virgin_islands = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_virgin_islands.add(*[button for button_row in buttons_virgin_islands for button in button_row])


#Список слов, на которые бот реагирует
messages_list = [
    '/start', '/help', '/countries', '/consultation', 'все страны', 'помощь', 'консультация специалиста',
    'виргинские острова', 'виргинские', 'virgin islands', 'virgin', 'dbhubycrbt jcnhjdf', 'dbhubycrbt',
    'гвинея', 'guinea', 'udbytz', 
    'конго', 'congo', 'rjyuj',
    'корея', 'korea', 'rjhtz',
    'самоа', 'samoa', 'cfvjf',
    'судан', 'sudan', 'celfy', 
    

    'абхазия', 'abkhazia', 'f,[fpbz',
    'австралия', 'australia', 'fdcnhfkbz',
    'австрия', 'austria', 'fdcnhbz',
    'азербайджан', 'azerbaijan', 'fpth,fql;fy',
    'албания', 'albania', 'fk,fybz',
    'алжир', 'algeria', 'fk;bh',
    'американские виргинские острова', 'united states virgin islands', 'fvthbrfycrbt b dbhubycrbt jcnhjdf',
    'американское самоа', 'american samoa', 'fvthbrfycrjt cfvjf',
    'ангилья', 'anguilla', 'fyubkmz',
    'ангола', 'angola', 'fyujkf',
    'андорра', 'andorra', 'fyljhhf',
    #'антарктида', 'antarctica', 'fynfhrnblf',
    'антигуа и барбуда', 'антигуа', 'antigua', 'fynbuef', 'antigua and barbuda', 'fynbuef b ,fh,elf',
    'аргентина', 'argentina', 'fhutynbyf',
    'армения', 'armenia', 'fhvtybz',
    'аруба', 'aruba', 'fhe,f',
    'афганистан', 'afghanistan', 'faufybcnfy',
    'багамские острова', 'багамы', 'bahamas', ',fufvcrbt jcnhjdf', ',fufvs',
    'бангладеш', 'bangladesh', ',fyukflti',
    'барбадос', 'barbados', ',fh,fljc',
    'бахрейн', 'bahrain', ',f[htqy',
    'белиз', 'belize', ',tkbp',
    'беларусь', 'белоруссия', 'belarus', ',tkfhecm', ',tkjheccbz',
    'бельгия', 'belgium', ',tkmubz',
    'бенин', 'benin', ',tyby',
    'бермудские острова', 'бермуды', 'bermuda islands', ',thvels', ',thvelcrbt jcnhjdf',
    'болгария', 'bulgaria', ',jkufhbz',
    'боливия', 'bolivia', ',jkbdbz',
    'босния и герцеговина', 'босния', 'bosnia', 'bosnia and herzegovina', ',jcybz', ',jcybz b uthwtujdbyf',
    'ботсвана', 'botswana', ',jncdfyf',
    'бразилия', 'brazil', ',hfpbkbz',
    'британские виргинские острова', 'british virgin islands', ',hbnfycrbt dbhubycrbt jcnhjdf',
    'бруней', 'brunei', ',heytq',
    'буркина-фасо', 'буркина фасо', 'буркина', 'фасо', 'burkina faso', 'burkina', 'faso', ',ehrbyf-afcj', ',ehrbyf afcj', ',ehrbyf', 'afcj',
    'бурунди', 'burundi', ',eheylb',
    'бутан', 'butane', ',enfy',
    'вануату', 'vanuatu', 'dfyefne', 
    'ватикан', 'vatican', 'dfnbrfy', 
    'великобритания', 'англия', 'great britain', 'united kingdom', 'fyukbz', 'dtkbrj,hbnfybz', 
    'венгрия', 'hungary', 'dtyuhbz', 
    'венесуэла', 'venezuela', 'dtytce\'kf', 
    'восточный тимор', 'тимор-лесте', 'тимор', 'east timor', 'timor-leste', 'timor leste', 'timor', 'djcnjxysq nbvjh', 'nbvjh-ktcnt', 'nbvjh',
    'вьетнам', 'vietnam', 'dmtnyfv', 
    'габон', 'gabon', 'uf,jy', 
    'гаити', 'haiti', 'ufbnb', 
    'гайана', 'guyana', 'ufqfyf', 
    'гамбия', 'gambia', 'ufv,bz', 
    'гана', 'ghana', 'ufyf', 
    'гватемала', 'guatemala', 'udfntvfkf', 
    'гвинейская республика', 'republic of guinea', 'udbytqcrfz htcge,kbrf', 
    'гвинея-бисау', 'гвинея бисау', 'guinea-bissau', 'guinea bissau', 'udbytz ,bcfe', 'udbytz-,bcfe', 
    'германия', 'germany', 'uthvfybz', 
    'гернси', 'guernsey', 'uthycb', 
    'гибралтар', 'gibraltar', 'ub,hfknfh', 
    'гондурас', 'honduras', 'ujylehfc', 
    'гонконг', 'hong kong', 'ujyrjyu', 
    'гренада', 'grenada', 'uhtyflf', 
    'гренландия', 'greenland', 'uhtykfylbz', 
    'греция', 'greece', 'uhtwbz', 
    'грузия', 'georgia', 'uhepbz', 
    'гуам', 'guam', 'uefv', 
    'дания', 'denmark', 'lfybz', 
    'конго-киншаса', 'демократическая республика конго', 'конго киншаса', 'congo kinshasa', 'congo-kinshasa', 'democratic republic of the congo', 'democratic republic of congo', 'ltvjrhfnbxtcrfz htcge,kbrf rjyuj', 'rjyuj-rbyifcf', 'rjyuj rbyifcf', 
    'джерси', 'jersey', 'l;thcb', 
    'джибути', 'djibouti', 'l;b,enb', 
    'доминика', 'dominica', 'ljvbybrf', 
    'доминикана', 'dominican republic', 'ljvbybrfyf', 
    'египет', 'egypt', 'tubgtn', 
    'замбия', 'zambia', 'pfv,bz', 
    'западное самоа', 'west samoa', 'pfgflyjt cfvjf', 
    'зимбабве', 'zimbabwe', 'pbv,f,dt', 
    'израиль', 'israel', 'bphfbkm', 
    'индия', 'india', 'bylbz', 
    'индонезия', 'indonesia', 'byljytpbz', 
    'иордания', 'jordan', 'bjhlfybz', 
    'ирак', 'iraq', 'bhfr', 
    'иран', 'iran', 'bhfy', 
    'ирландия', 'ireland', 'bhkfylbz', 
    'исландия', 'iceland', 'bckfylbz', 
    'испания', 'spain', 'bcgfybz', 
    'италия', 'italy', 'bnfkbz', 
    'йемен', 'yemen', 'qtvty', 
    'кабо-верде', 'кабо верде', 'кабо', 'верде', 'cape verde', 'cape', 'verde', 'rf,j-dthlt', 'rf,j dthlt', 'rf,j', 'dthlt',
    'казахстан', 'kazakhstan', 'rfpf[cnfy', 
    'каймановы острова', 'кайман', 'каймановы', 'острова кайман', 'cayman islands', 'cayman', 'rfqvfyjds jcnhjdf', 'jcnhjdf rfqvfy', 'rfqvfy', 'rfqvfyjds', 
    'камбоджа', 'cambodia', 'rfv,jl;f', 
    'камерун', 'cameroon', 'rfvthey', 
    'канада', 'canada', 'rfyflf', 
    'катар', 'qatar', 'rfnfh', 
    'кения', 'kenya', 'rtybz', 
    'кипр', 'cyprus', 'rbgh', 
    'кыргызстан', 'kyrgyzstan', 'rshuspcnfy', 'киргизия', 'rbhubpbz',
    'кирибати', 'kiribati', 'rbhb,fnb', 
    'китай', 'кнр', 'china', 'ryh', 'rbnfq', 
    'северная корея', 'кндр', 'north korea', 'rylh', 'ctdthyfz rjhtz', 
    'колумбия', 'colombia', 'rjkev,bz', 
    #'кокосовые острова', 'cocos islands', 'rjrjcjdst jcnhjdf', 
    'коморские острова', 'коморские', 'comoros', 'rjvjhcrbt jcnhjdf', 'rjvjhcrbt',
    'республика конго', 'конго браззавиль', 'конго-браззавиль', 'congo brazzaville', 'congo-brazzaville', 'republic of the congo', 'republic of congo', 'rjyuj-,hfppfdbkm', 'rjyuj ,hfppfdbkm', 'htcge,kbrf rjyuj', 
    'южная корея', 'south korea', '.;yfz rjhtz', 
    'коста-рика', 'коста рика', 'costa rica', 'rjcnf-hbrf', 'rjcnf hbrf', 
    'кот-д’ивуар', 'котдивуар', 'кот дивуар', 'кот-дивуар', 'ivory coast', 'rjn-l\'bdefh', 'rjnlbdefh', 'rjn-lbdefh', 'rjn lbdefh', 
    'куба', 'cuba', 're,f', 
    'кувейт', 'kuwait', 'redtqn', 
    'кюрасао', 'curacao', 'r.hfcfj', 
    'лаос', 'laos', 'kfjc', 
    'латвия', 'latvia', 'kfndbz', 
    'лесото', 'lesotho', 'ktcjnj', 
    'либерия', 'liberia', 'kb,thbz', 
    'ливан', 'lebanon', 'kbdfy', 
    'ливия', 'libya', 'kbdbz', 
    'литва', 'lithuania', 'kbndf', 
    'лихтенштейн', 'liechtenstein', 'kb[ntyintqy', 
    'люксембург', 'luxemburg', 'k.rctv,ehu', 
    'маврикий', 'mauritius', 'vfdhbrbq', 
    'мавритания', 'mauritania', 'vfdhbnfybz', 
    'мадагаскар', 'madagascar', 'vflfufcrfh', 
    'макао', 'macau', 'vfrfj', 
    'македония', 'северная македония', 'macedonia', 'northern macedonia', 'ctdthyfz vfrtljybz', 'vfrtljybz', 
    'малави', 'malawi', 'vfkfdb', 
    'малайзия', 'malaysia', 'vfkfqpbz', 
    'мали', 'mali', 'vfkb', 
    'мальдивы', 'maldives', 'vfkmlbds', 
    'мальта', 'malta', 'vfkmnf', 
    'марокко', 'morocco', 'vfhjrrj', 
    #'мартиника', 'martinique', 'vfhnbybrf', 
    'маршалловы острова', 'маршалловы', 'marshall islands', 'marshall', 'vfhifkkjds jcnhjdf', 'vfhifkkjds',
    'мексика', 'mexico', 'vtrcbrf', 
    'микронезия', 'micronesia', 'vbrhjytpbz', 
    'мозамбик', 'mozambique', 'vjpfv,br', 
    'молдавия', 'молдова', 'moldova', 'vjkljdf', 'vjklfdbz', 
    'монако', 'monaco', 'vjyfrj', 
    'монголия', 'mongolia', 'vjyujkbz', 
    'монтсеррат', 'montserrat', 'vjyncthhfn', 
    'мьянма', 'myanmar', 'vmzyvf', 
    'намибия', 'namibia', 'yfvb,bz', 
    #'народная республика конго', 'national republic of congo', 'national republic of the congo', 'yfhjlyfz htcge,kbrf rjyuj', 
    'науру', 'nauru', 'yfehe', 
    'непал', 'nepal', 'ytgfk', 
    'нигер', 'niger', 'ybuth', 
    'нигерия', 'nigeria', 'ybuthbz', 
    'нидерланды', 'netherlands', 'yblthkfyls', 
    'никарагуа', 'nicaragua', 'ybrfhfuef', 
    'ниуэ', 'niue', 'ybe\'', 
    'новая зеландия', 'new zealand', 'yjdfz ptkfylbz', 
    'новая каледония', 'new caledonia', 'yjdfz rfktljybz', 
    'норвегия', 'norway', 'yjhdtubz', 
    'оаэ', 'эмираты', 'объединённые арабские эмираты', 'объединенные арабские эмираты', 'united arab emirates', 'uae', 'jf\'', '\'vbhfns', 'j,]tlbytyyst fhf,crbt \'vbhfns', 
    'оман', 'oman', 'jvfy', 
    'остров бонайре', 'бонайре', 'bonaira', 'bonaira island', 'jcnhjd ,jyfqht', ',jyfqht', 
    'острова кука', 'cook islands', 'jcnhjdf rerf', 
    'острова норфолк', 'норфолк', 'norfolk islands', 'norfolk', 'jcnhjdf yjhajkr', 'yjhajkr',
    'остров саба', 'саба', 'saba island', 'saba', 'jcnhjd cf,f', 'cf,f', 
    'остров святой елены', 'st. helena island', 'st helena island', 'saint helena island', 'jcnhjd cdznjq tktys', 
    #'остров сен-бартелеми', 'сен бартелеми', 'сен-бартелеми', 'saint-bartelemi island', 'saint-bartelemi', 'saint bartelemi', 'st bartelemi', 'cty ,fhntktvb', 'cty-,fhntktvb', 'jcnhjd cty-,fhntktvb', 
    'остров сен-мартен', 'сен-мартен', 'сен мартен', 'saint-martin island', 'saint-martin', 'st martin', 'st. martin', 'saint martin', 'jcnhjd cty-vfhnty', 'cty-vfhnty', 'cty vfhnty', 
    'остров синт-эстатиус', 'синт-эстатиус', 'синт эстатиус', 'sint estatius island', 'sint estatius', 'sint-estatius', 'jcnhjd cbyn-\'cnfnbec', 'cbyn-\'cnfnbec', 'cbyn \'cnfnbec', 
    #'острова уоллис и футуна', 'уоллис и футуна', 'wallis and futuna islands', 'wallis and futuna', 'jcnhjdf ejkkbc b aeneyf', 'ejkkbc b aeneyf', 
    #'острова херд и макдональд', 'херд и макдональд', 'herd and macdonald islands', 'herd and macdonald', 'jcnhjdf [thl b vfrljyfkl', '[thl b vfrljyfkl', 
    'пакистан', 'pakistan', 'gfrbcnfy', 
    'палау', 'palau', 'gfkfe', 
    #'палестина', 'palestine', 'gfktcnbyf', 
    'панама', 'panama', 'gfyfvf', 
    'папуа-новая гвинея', 'папуа новая гвинея', 'папуа', 'новая гвинея', 'papua', 'new guinea', 'papua new guinea', 'papua-new guinea', 'gfgef-yjdfz udbytz', 'gfgef yjdfz udbytz', 'yjdfz udbytz', 'gfgef', 
    'парагвай', 'paraguay', 'gfhfudfq', 
    'перу', 'peru', 'gthe', 
    'польша', 'poland', 'gjkmif', 
    'португалия', 'portugal', 'gjhneufkbz', 
    'пуэрто-рико', 'пуэрто рико', 'puerto rico', 'puerto-rico', 'ge\'hnj hbrj', 'ge\'hnj-hbrj', 
    'реюньон', 'reunion', 'ht.ymjy', 
    #'россия', 'russia', 'hjccbz', 
    'руанда', 'rwanda', 'hefylf', 
    'румыния', 'romania', 'hevsybz', 
    'сальвадор', 'salvador', 'cfkmdfljh', 
    'сан-марино', 'сан марино', 'san marino', 'cfy vfhbyj', 'cfy-vfhbyj', 
    'сан-томе и принсипи', 'сан-томе', 'сан томе', 'принсипи', 'sao tome and principe', 'principe', 'sao tome', 'cfy-njvt b ghbycbgb', 'cfy-njvt', 'cfy njvt', 'ghbycbgb', 'cfy njvt b ghbycbgb', 
    'саудовская аравия', 'saudi arabia', 'cfeljdcrfz fhfdbz', 
    'северные марианские острова', 'марианские острова', 'марианские', 'northern mariana islands', 'mariana islands', 'mariana', 'ctdthyst vfhbfycrbt jcnhjdf', 'vfhbfycrbt jcnhjdf',  'vfhbfycrbt',
    'сейшельские острова', 'сейшелы', 'seychelles', 'ctqitkmcrbt jcnhjdf', 'ctqitks', 
    'сенегал', 'senegal', 'ctytufk', 
    #'сен-пьер и микелон', 'сен-пьер', 'сен пьер', 'микелон', 'miquelon', 'saint-pierre and miquelon', 'saint pierre', 'saint-pierre', 'vbrtkjy', 'cty-gmth b vbrtkjy', 'cty-gmth', 'cty gmth', 
    'сент-винсент и гренадины', 'сент-винсент', 'сент винсент', 'гренадины', 'st. vincent', 'saint vincent and grenadines', 'saint vincent', 'grenadines', 'ctyn-dbyctyn b uhtyflbys', 'uhtyflbys', 'ctyn dbyctyn', 'ctyn-dbyctyn', 
    'сент-китс и невис', 'сент-китс', 'сент китс', 'невис', 'saint kitts and nevis', 'saint kitts', 'nevis', 'ctyn-rbnc b ytdbc', 'ctyn-rbnc', 'ctyn rbnc', 'ytdbc', 
    'сент-люсия', 'сент люсия', 'saint lucia', 'ctyn k.cbz', 'ctyn-k.cbz', 
    'сербия', 'serbia', 'cth,bz', 
    'сингапур', 'singapore', 'cbyufgeh', 
    'сирия', 'syria', 'cbhbz', 
    'словакия', 'slovakia', 'ckjdfrbz', 
    'словения', 'slovenia', 'ckjdtybz', 
    'соломоновы острова', 'соломоновы', 'solomon islands', 'solomon', 'cjkjvjyjds jcnhjdf', 'cjkjvjyjds', 
    'сомали', 'somalia', 'cjvfkb', 
    'республика судан', 'republic of sudan', 'htcge,kbrf celfy', 
    'суринам', 'suriname', 'cehbyfv', 
    'сша', 'америка', 'соединенные штаты америки', 'united states of america', 'usa', 'america', 'fvthbrf', 'cif', 'cjtlbytyyst infns fvthbrb', 
    'сьерра-леоне', 'сьерра леоне', 'sierra leone', 'cmthhf ktjyt', 'cmthhf-ktjyt', 
    'таджикистан', 'tajikistan', 'nfl;brbcnfy', 
    'тайвань', 'taiwan', 'nfqdfym', 
    'таиланд', 'тайланд', 'thailand', 'nfqkfyl', 'nfbkfyl', 
    'танзания', 'tanzania', 'nfypfybz', 
    'теркс и кайкос', 'turks and caicos', 'nthrc b rfqrjc', 
    'того', 'togo', 'njuj', 
    #'токелау', 'tokelau', 'njrtkfe', 
    'тонга', 'tonga', 'njyuf', 
    'тринидад и тобаго', 'тринидад', 'тобаго', 'trinidad and tobago', 'trinidad', 'tobago', 'nhbyblfl b nj,fuj', 'nhbyblfl', 'nj,fuj', 
    'тувалу', 'tuvalu', 'nedfke', 
    'тунис', 'tunisia', 'neybc', 
    'туркменистан', 'turkmenistan', 'nehrvtybcnfy', 
    'турция', 'turkey', 'nehwbz',
    'уганда', 'uganda', 'eufylf',
    'узбекистан', 'uzbekistan', 'ep,trbcnfy',
    'украина', 'ukraine', 'erhfbyf',
    'уругвай', 'uruguay', 'eheudfq',
    #'фарерские острова', 'faroe islands', 'afhthcrbt jcnhjdf',
    'фиджи', 'fiji', 'abl;b',
    'филиппины', 'philippines', 'abkbggbys',
    'финляндия', 'finland', 'abykzylbz',
    'фолклендские острова', 'фолклендские', 'falkland islands', 'falkland', 'ajkrktylcrbt jcnhjdf', 'ajkrktylcrbt',
    'франция', 'france', 'ahfywbz',
    #'французская гваделупа', 'гваделупа', 'guadeloupe', 'french guadeloupe', 'udfltkegf', 'ahfywepcrfz udfltkegf',
    'французская гвиана', 'гвиана', 'french guiana', 'guiana', 'udbfyf', 'ahfywepcrfz udbfyf',
    'французская полинезия', 'полинезия', 'polynesia', 'french polynesia', 'gjkbytpbz', 'ahfywepcrfz gjkbytpbz',
    'хорватия', 'croatia', '[jhdfnbz',
    'центральноафриканская республика', 'цар', 'central african republic', 'car', 'wtynhfkmyjfahbrfycrfz htcge,kbrf', 'wfh',
    'чад', 'chad', 'xfl',
    'черногория', 'montenegro', 'xthyjujhbz',
    'чехия', 'czech', 'czech republic', 'xt[bz',
    'чили', 'chile', 'xbkb',
    'швейцария', 'switzerland', 'idtqwfhbz',
    'швеция', 'sweden', 'idtwbz',
    #'шпицберген', 'svalbard', 'spitsbergen', 'igbw,thuty',
    'шри-ланка', 'шри ланка', 'sri lanka', 'ihb-kfyrf', 'ihb kfyrf',
    'эквадор', 'ecuador', '\'rdfljh',
    'экваториальная гвинея', 'equatorial guinea', '\'rdfnjhbfkmyfz udbytz',
    'эритрея', 'erythrea', '\'hbnhtz',
    'эсватини', 'eswatini', '\'cdfnbyb',
    'эстония', 'estonia', '\'cnjybz',
    'эфиопия', 'ethiopia', '\'abjgbz',
    'юар', 'south africa', '.fh',
    'южный судан', 'south sudan', '.;ysq celfy',
    'ямайка', 'jamaica', 'zvfqrf',
    'япония', 'japan', 'zgjybz'
]


#Обработка ошибок(некорректных запросов)
@dp.message_handler(lambda message: message.text.lower() not in messages_list)
async def handle_messages(message: Message):
    command="Incorrect input"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command + " (" +  message.text + ")"])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command + " (" +  message.text + ")"}')
    
    await message.answer("Упс, такой страны я не знаю… Попробуйте ввести название страны по-другому или нажмите на кнопку «Все страны», чтобы найти её.", reply_markup=keyboard_menu)

#Начало
@dp.message_handler(commands=["start"])
async def start(message: Message):
    command="Start"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{user_full_name}, добро пожаловать в @simpleflybot – телеграм бот, который поможет спланировать безопасное и комфортное путешествие!\n\n<b>Введите название страны</b>, и вы узнаете требования к паспорту, визе, медицинским документам и многому другому!", reply_markup=keyboard_menu)

#Блок страны
@dp.message_handler(lambda message: message.text.lower() == "/countries" or message.text.lower() == "countries"or message.text.lower() == "все страны")
async def countries_by_search(message: Message):
    command="All countries"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/123-03-04-51')}" f"В этой статье вы найдете список всех стран.", reply_markup=keyboard_menu)

#Блок помощь
@dp.message_handler(lambda message: message.text.lower() == "помощь" or message.text.lower() == "/help" or message.text.lower() == "help")
async def help_by_search(message: Message):
    command="Help"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    text = hlink('телеграм канал', 'https://t.me/sittype/5')
    await message.answer("Введите страну назначения, чтобы узнать о паспортно-визовых требованиях и другую важную информацию, необходимую для въезда в страну. Например: Сербия. У вас вопрос посложнее? Напишите нам в " + text + ", и мы обязательно поможем!", reply_markup=keyboard_menu, disable_web_page_preview = True)

#Блок консультация
@dp.message_handler(lambda message: message.text.lower() == "консультация специалиста" or message.text.lower() == "consultation" or message.text.lower() == "/consultation")
async def consultation_by_search(message: Message):
    command="Consultation"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    text = hlink('телеграм канал', 'https://t.me/sittype/5')
    await message.answer("Прочитали статью, но все еще остались вопросы? Напишите нам в " + text + ", и мы обязательно поможем!", disable_web_page_preview = True, reply_markup=keyboard_menu)

#Поиск стран: 
# 
# Виргинские острова
@dp.message_handler(lambda message: message.text.lower() == 'виргинские острова' or message.text.lower() == 'виргинские' or message.text.lower() == 'virgin islands' or message.text.lower() == 'virgin' or message.text.lower() == 'dbhubycrbt jcnhjdf'  or message.text.lower() == 'dbhubycrbt')
async def virgin_islands_by_search(message: Message): 
    command="Virgin islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer("Ого! По вашему запросу нашлось несколько результатов. Выберите нужный:", reply_markup=keyboard_virgin_islands)

# Гвинея
@dp.message_handler(lambda message: message.text.lower() == 'гвинея' or message.text.lower() == 'guinea' or message.text.lower() == 'udbytz')
async def guinea_by_search(message: Message): 
    command="Guinea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer("Ого! По вашему запросу нашлось несколько результатов. Выберите нужный:", reply_markup=keyboard_guinea)

# Конго
@dp.message_handler(lambda message: message.text.lower() == 'конго' or message.text.lower() == 'congo' or message.text.lower() == 'rjyuj')
async def congo_by_search(message: Message): 
    command="Congo"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer("Ого! По вашему запросу нашлось несколько результатов. Выберите нужный:", reply_markup=keyboard_congo)

# Корея
@dp.message_handler(lambda message: message.text.lower() == 'корея' or message.text.lower() == 'korea' or message.text.lower() == 'rjhtz')
async def korea_by_search(message: Message): 
    command="Korea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer("Ого! По вашему запросу нашлось несколько результатов. Выберите нужный:", reply_markup=keyboard_korea)

# Самоа
@dp.message_handler(lambda message: message.text.lower() == 'самоа' or message.text.lower() == 'samoa' or message.text.lower() == 'cfvjf')
async def samoa_by_search(message: Message): 
    command="Samoa"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer("Ого! По вашему запросу нашлось несколько результатов. Выберите нужный:", reply_markup=keyboard_samoa)

# Судан
@dp.message_handler(lambda message: message.text.lower() == 'судан' or message.text.lower() == 'sudan' or message.text.lower() == 'celfy')
async def sudan_by_search(message: Message): 
    command="Sudan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer("Ого! По вашему запросу нашлось несколько результатов. Выберите нужный:", reply_markup=keyboard_sudan)



# Абхазия
@dp.message_handler(lambda message: message.text.lower() == 'абхазия' or message.text.lower() == 'abkhazia' or message.text.lower() == 'f,[fpbz')
async def abkhazia_by_search(message: Message): 
    command="Abkhazia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pravila-vezda-v-Abhaziyu-04-26')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Абхазию.", reply_markup=keyboard_menu)

# Австралия
@dp.message_handler(lambda message: message.text.lower() == 'австралия' or message.text.lower() == 'australia' or message.text.lower() == 'fdcnhfkbz')
async def australia_by_search(message: Message): 
    command="Australia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pravila-vezda-v-Avstraliyu-04-22')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Австралию.", reply_markup=keyboard_menu)

# Австрия
@dp.message_handler(lambda message: message.text.lower() == 'австрия' or message.text.lower() == 'austria' or message.text.lower() == 'fdcnhbz')
async def austria_by_search(message: Message): 
    command="Austria"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pravila-vezda-v-Avstriyu-04-23')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Австрию.", reply_markup=keyboard_menu)

# Азербайджан
@dp.message_handler(lambda message: message.text.lower() == 'азербайджан' or message.text.lower() == 'azerbaijan' or message.text.lower() == 'fpth,fql;fy')
async def azerbaijan_by_search(message: Message): 
    command="Azerbaijan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pravila-vezda-v-Azerbajdzhan-04-23')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Азербайджан.", reply_markup=keyboard_menu)

# Албания
@dp.message_handler(lambda message: message.text.lower() == 'албания' or message.text.lower() == 'albania' or message.text.lower() == 'fk,fybz')
async def albania_by_search(message: Message): 
    command="Albania"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pravila-vezda-v-Albaniyu-04-23')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Албанию.", reply_markup=keyboard_menu)

# Алжир
@dp.message_handler(lambda message: message.text.lower() == 'алжир' or message.text.lower() == 'algeria' or message.text.lower() == 'fk;bh')
async def algeria_by_search(message: Message): 
    command="Algeria"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pravila-vezda-v-Alzhir-04-23')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Алжир.", reply_markup=keyboard_menu)

# Американские Виргинские острова
@dp.message_handler(lambda message: message.text.lower() == 'американские виргинские острова' or message.text.lower() == 'united states virgin islands' or message.text.lower() == 'fvthbrfycrbt dbhubycrbt jcnhjdf')
async def united_states_virgin_islands_by_search(message: Message): 
    command="United States Virgin Islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Amerikanskie-Virginskie-ostrova-poehali-04-26')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Американские Виргинские острова.", reply_markup=keyboard_menu)

# Американское Самоа
@dp.message_handler(lambda message: message.text.lower() == 'американское самоа' or message.text.lower() == 'american samoa' or message.text.lower() == 'fvthbrfycrjt cfvjf')
async def american_samoa_by_search(message: Message): 
    command="American Samoa"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Amerikanskoe-Samoa-poehali-04-26')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Американское Самоа.", reply_markup=keyboard_menu)

# Ангилья
@dp.message_handler(lambda message: message.text.lower() == 'ангилья' or message.text.lower() == 'anguilla' or message.text.lower() == 'fyubkmz')
async def anguilla_by_search(message: Message): 
    command="Anguilla"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Angilya-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ангилью.", reply_markup=keyboard_menu)

# Ангола
@dp.message_handler(lambda message: message.text.lower() == 'ангола' or message.text.lower() == 'angola' or message.text.lower() == 'fyujkf')
async def angola_by_search(message: Message): 
    command="Angola"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Angola-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Анголу.", reply_markup=keyboard_menu)

# Андорра
@dp.message_handler(lambda message: message.text.lower() == 'андорра' or message.text.lower() == 'andorra' or message.text.lower() == 'fyljhhf')
async def andorra_by_search(message: Message): 
    command="Andorra"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Andorra-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Андорру.", reply_markup=keyboard_menu)

"""
# Антарктида
@dp.message_handler(lambda message: message.text.lower() == 'антарктида' or message.text.lower() == 'antarctica' or message.text.lower() == 'fynfhrnblf')
async def antarctica_by_search(message: Message): 
    command="Antarctica"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Antarktida-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Антарктиду.", reply_markup=keyboard_menu)
"""

# Антигуа и Барбуда
@dp.message_handler(lambda message: message.text.lower() == 'антигуа и барбуда' or message.text.lower() == 'антигуа' or message.text.lower() == 'antigua' or message.text.lower() == 'antigua and barbuda' or message.text.lower() == 'fynbuef' or message.text.lower() == 'fynbuef b ,fh,elf')
async def antigua_and_barbuda_by_search(message: Message): 
    command="Antigua and Barbuda"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Antigua-i-Barbuda-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Антигуа и Барбуда.", reply_markup=keyboard_menu)

# Аргентина
@dp.message_handler(lambda message: message.text.lower() == 'аргентина' or message.text.lower() == 'argentina' or message.text.lower() == 'fhutynbyf')
async def argentina_by_search(message: Message): 
    command="Argentina"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Argentina-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Аргентину.", reply_markup=keyboard_menu)

# Армения
@dp.message_handler(lambda message: message.text.lower() == 'армения' or message.text.lower() == 'armenia' or message.text.lower() == 'fhvtybz')
async def armenia_by_search(message: Message): 
    command="Armenia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Armeniya-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Армению.", reply_markup=keyboard_menu)

# Аруба
@dp.message_handler(lambda message: message.text.lower() == 'аруба' or message.text.lower() == 'aruba' or message.text.lower() == 'fhe,f')
async def aruba_by_search(message: Message): 
    command="Aruba"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Aruba-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Арубу.", reply_markup=keyboard_menu)

# Афганистан
@dp.message_handler(lambda message: message.text.lower() == 'афганистан' or message.text.lower() == 'afghanistan' or message.text.lower() == 'faufybcnfy')
async def afghanistan_by_search(message: Message): 
    command="Afghanistan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Afganistan-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Афганистан.", reply_markup=keyboard_menu)

# Багамские острова (Багамы)
@dp.message_handler(lambda message: message.text.lower() == 'багамские острова' or message.text.lower() == 'багамы' or message.text.lower() == 'bahamas' or message.text.lower() == ',fufvcrbt jcnhjdf' or message.text.lower() == ',fufvs')
async def bahamas_by_search(message: Message): 
    command="Bahamas"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Bagamskie-ostrova-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Багамские острова.", reply_markup=keyboard_menu)

# Бангладеш
@dp.message_handler(lambda message: message.text.lower() == 'бангладеш' or message.text.lower() == 'bangladesh' or message.text.lower() == ',fyukflti')
async def bangladesh_by_search(message: Message): 
    command="Bangladesh"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Bangladesh-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бангладеш.", reply_markup=keyboard_menu)

# Барбадос
@dp.message_handler(lambda message: message.text.lower() == 'барбадос' or message.text.lower() == 'barbados' or message.text.lower() == ',fh,fljc')
async def barbados_by_search(message: Message): 
    command="Barbados"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Barbados-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Барбадос.", reply_markup=keyboard_menu)

# Бахрейн
@dp.message_handler(lambda message: message.text.lower() == 'бахрейн' or message.text.lower() == 'bahrain' or message.text.lower() == ',f[htqy')
async def bahrain_by_search(message: Message): 
    command="Bahrain"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Bahrejn-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бахрейн.", reply_markup=keyboard_menu)

# Белиз
@dp.message_handler(lambda message: message.text.lower() == 'белиз' or message.text.lower() == 'belize' or message.text.lower() == ',tkbp')
async def belize_by_search(message: Message): 
    command="Belize"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Beliz-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Белиз.", reply_markup=keyboard_menu)

# Беларусь (Белоруссия)
@dp.message_handler(lambda message: message.text.lower() == 'беларусь' or message.text.lower() == 'белоруссия' or message.text.lower() == 'belarus' or message.text.lower() == ',tkfhecm' or message.text.lower() == ',tkjheccbz')
async def belarus_by_search(message: Message): 
    command="Belarus"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Respublika-Belarus-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Беларусь.", reply_markup=keyboard_menu)

# Бельгия
@dp.message_handler(lambda message: message.text.lower() == 'бельгия' or message.text.lower() == 'belgium' or message.text.lower() == ',tkmubz')
async def belgium_by_search(message: Message): 
    command="Belgium"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Belgiya-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бельгию.", reply_markup=keyboard_menu)

# Бенин
@dp.message_handler(lambda message: message.text.lower() == 'бенин' or message.text.lower() == 'benin' or message.text.lower() == ',tyby')
async def benin_by_search(message: Message): 
    command="Benin"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Benin-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бенин.", reply_markup=keyboard_menu)

# Бермудские острова (Бермуды)
@dp.message_handler(lambda message: message.text.lower() == 'бермудские острова' or message.text.lower() == 'бермуды' or message.text.lower() == 'bermuda islands' or message.text.lower() == ',thvels' or message.text.lower() == ',thvelcrbt jcnhjdf')
async def bermuda_islands_by_search(message: Message): 
    command="Bermuda Islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Bermudskie-ostrova-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Бермудские острова.", reply_markup=keyboard_menu)

# Болгария
@dp.message_handler(lambda message: message.text.lower() == 'болгария' or message.text.lower() == 'bulgaria' or message.text.lower() == ',jkufhbz')
async def bulgaria_by_search(message: Message): 
    command="Bulgaria"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Bolgariya-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Болгарию.", reply_markup=keyboard_menu)

# Боливия
@dp.message_handler(lambda message: message.text.lower() == 'боливия' or message.text.lower() == 'bolivia' or message.text.lower() == ',jkbdbz')
async def bolivia_by_search(message: Message): 
    command="Bolivia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Boliviya-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Боливию.", reply_markup=keyboard_menu)

# Босния и Герцеговина
@dp.message_handler(lambda message: message.text.lower() == 'босния и герцеговина' or message.text.lower() == 'босния' or message.text.lower() == 'bosnia' or message.text.lower() == 'bosnia and herzegovina' or message.text.lower() == ',jcybz' or message.text.lower() == ',jcybz b uthwtujdbyf')
async def bosnia_and_herzegovina_by_search(message: Message): 
    command="Bosnia and Herzegovina"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Bosniya-i-Gercegovina-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Боснию и Герцеговину.", reply_markup=keyboard_menu)

# Ботсвана
@dp.message_handler(lambda message: message.text.lower() == 'ботсвана' or message.text.lower() == 'botswana' or message.text.lower() == ',jncdfyf')
async def botswana_by_search(message: Message): 
    command="Botswana"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Botsvana-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ботсвану.", reply_markup=keyboard_menu)

# Бразилия
@dp.message_handler(lambda message: message.text.lower() == 'бразилия' or message.text.lower() == 'brazil' or message.text.lower() == ',hfpbkbz')
async def brazil_by_search(message: Message): 
    command="Brazil"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Braziliya-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бразилию.", reply_markup=keyboard_menu)

# Британские Виргинские Острова
@dp.message_handler(lambda message: message.text.lower() == 'британские виргинские острова' or message.text.lower() == 'british virgin islands' or message.text.lower() == ',hbnfycrbt dbhubycrbt jcnhjdf')
async def british_virgin_islands_by_search(message: Message): 
    command="British Virgin Islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Britanskie-Virginskie-Ostrova-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Британские Виргинские Острова.", reply_markup=keyboard_menu)

# Бруней
@dp.message_handler(lambda message: message.text.lower() == 'бруней' or message.text.lower() == 'brunei' or message.text.lower() == ',heytq')
async def brunei_by_search(message: Message): 
    command="Brunei"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Brunej-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бруней.", reply_markup=keyboard_menu)

# Буркина-Фасо
@dp.message_handler(lambda message: message.text.lower() == 'буркина-фасо' or message.text.lower() == 'буркина фасо' or message.text.lower() == 'буркина' or message.text.lower() == 'фасо' or message.text.lower() == 'burkina faso' or message.text.lower() == 'burkina' or message.text.lower() == 'faso' or message.text.lower() == ',ehrbyf-afcj' or message.text.lower() == ',ehrbyf' or message.text.lower() == 'afcj' or message.text.lower() == ',ehrbyf afcj')
async def burkina_faso_by_search(message: Message): 
    command="Burkina Faso"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Burkina-Faso-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Буркина-Фасо.", reply_markup=keyboard_menu)

# Бурунди
@dp.message_handler(lambda message: message.text.lower() == 'бурунди' or message.text.lower() == 'burundi' or message.text.lower() == ',eheylb')
async def burundi_by_search(message: Message): 
    command="Burundi"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Burundi-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бурунди.", reply_markup=keyboard_menu)

# Бутан
@dp.message_handler(lambda message: message.text.lower() == 'бутан' or message.text.lower() == 'butane' or message.text.lower() == ',enfy')
async def butane_by_search(message: Message): 
    command="Butane"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Butan-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Бутан.", reply_markup=keyboard_menu)

# Вануату
@dp.message_handler(lambda message: message.text.lower() == 'вануату' or message.text.lower() == 'vanuatu' or message.text.lower() == 'dfyefne')
async def vanuatu_by_search(message: Message):
    command="Vanuatu"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Vanuatu-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Вануату.", reply_markup=keyboard_menu)

# Ватикан
@dp.message_handler(lambda message: message.text.lower() == 'ватикан' or message.text.lower() == 'vatican' or message.text.lower() == 'dfnbrfy')
async def vatican_by_search(message: Message):
    command="Vatican"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Vatikan-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ватикан.", reply_markup=keyboard_menu)

# ??? Великобритания
@dp.message_handler(lambda message: message.text.lower() == 'великобритания' or message.text.lower() == 'англия' or message.text.lower() == 'great britain' or message.text.lower() == 'united kingdom' or message.text.lower() == 'fyukbz' or message.text.lower() == 'dtkbrj,hbnfybz')
async def united_kingdom_by_search(message: Message):
    command="United Kingdom"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Velikobritaniya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Великобританию.", reply_markup=keyboard_menu)

# Венгрия
@dp.message_handler(lambda message: message.text.lower() == 'венгрия' or message.text.lower() == 'hungary' or message.text.lower() == 'dtyuhbz')
async def hungary_by_search(message: Message):
    command="Hungary"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Vengriya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Венгрию.", reply_markup=keyboard_menu)

# Венесуэла
@dp.message_handler(lambda message: message.text.lower() == 'венесуэла' or message.text.lower() == 'venezuela' or message.text.lower() == 'dtytce\'kf')
async def venezuela_by_search(message: Message):
    command="Venezuela"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Venesuehla-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Венесуэлу.", reply_markup=keyboard_menu)

# Восточный Тимор (Тимор-Лесте)
@dp.message_handler(lambda message: message.text.lower() == 'восточный тимор' or message.text.lower() == 'тимор-лесте' or message.text.lower() == 'тимор' or message.text.lower() == 'east timor' or message.text.lower() == 'timor-leste' or message.text.lower() == 'timor leste' or message.text.lower() == 'timor' or message.text.lower() == 'djcnjxysq nbvjh' or message.text.lower() == 'nbvjh-ktcnt' or message.text.lower() == 'nbvjh')
async def east_timor_by_search(message: Message):
    command="East Timor"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Vostochnyj-Timor-Timor-Leste-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Восточный Тимор.", reply_markup=keyboard_menu)

# Вьетнам
@dp.message_handler(lambda message: message.text.lower() == 'вьетнам' or message.text.lower() == 'vietnam' or message.text.lower() == 'dmtnyfv')
async def vietnam_by_search(message: Message):
    command="Vietnam"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Vetnam-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда во Вьетнам.", reply_markup=keyboard_menu)

# Габон
@dp.message_handler(lambda message: message.text.lower() == 'габон' or message.text.lower() == 'gabon' or message.text.lower() == 'uf,jy')
async def gabon_by_search(message: Message):
    command="Gabon"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gabon-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Габон.", reply_markup=keyboard_menu)

# Гаити
@dp.message_handler(lambda message: message.text.lower() == 'гаити' or message.text.lower() == 'haiti' or message.text.lower() == 'ufbnb')
async def haiti_by_search(message: Message):
    command="Haiti"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gaiti-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Гаити.", reply_markup=keyboard_menu)

# Гайана
@dp.message_handler(lambda message: message.text.lower() == 'гайана' or message.text.lower() == 'guyana' or message.text.lower() == 'ufqfyf')
async def guyana_by_search(message: Message):
    command="Guyana"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gajana-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гайану.", reply_markup=keyboard_menu)

# Гамбия
@dp.message_handler(lambda message: message.text.lower() == 'гамбия' or message.text.lower() == 'gambia' or message.text.lower() == 'ufv,bz')
async def gambia_by_search(message: Message):
    command="Gambia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gambiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гамбию.", reply_markup=keyboard_menu)

# Гана
@dp.message_handler(lambda message: message.text.lower() == 'гана' or message.text.lower() == 'ghana' or message.text.lower() == 'ufyf')
async def ghana_by_search(message: Message):
    command="Ghana"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gana-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гану.", reply_markup=keyboard_menu)

# Гватемала
@dp.message_handler(lambda message: message.text.lower() == 'гватемала' or message.text.lower() == 'guatemala' or message.text.lower() == 'udfntvfkf')
async def guatemala_by_search(message: Message):
    command="Guatemala"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gvatemala-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гватемалу.", reply_markup=keyboard_menu)

# Гвинейская Республика
@dp.message_handler(lambda message: message.text.lower() == 'гвинейская республика' or message.text.lower() == 'republic of guinea' or message.text.lower() == 'udbytqcrfz htcge,kbrf')
async def republic_of_guinea_by_search(message: Message):
    command="Republic of Guinea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gvineya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гвинейскую Республику.", reply_markup=keyboard_menu)

# Гвинея-Бисау
@dp.message_handler(lambda message: message.text.lower() == 'гвинея-бисау' or message.text.lower() == 'гвинея бисау' or message.text.lower() == 'guinea-bissau' or message.text.lower() == 'guinea bissau' or message.text.lower() == 'udbytz ,bcfe' or message.text.lower() == 'udbytz-,bcfe')
async def guinea_bissau_by_search(message: Message):
    command="Guinea-Bissau"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gvineya-Bisau-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гвинею-Бисау.", reply_markup=keyboard_menu)

# Германия
@dp.message_handler(lambda message: message.text.lower() == 'германия' or message.text.lower() == 'germany' or message.text.lower() == 'uthvfybz')
async def germany_by_search(message: Message):
    command="Germany"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Germaniya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Германию.", reply_markup=keyboard_menu)

# Гернси
@dp.message_handler(lambda message: message.text.lower() == 'гернси' or message.text.lower() == 'guernsey' or message.text.lower() == 'uthycb')
async def guernsey_by_search(message: Message):
    command="Guernsey"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gernsi-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гернси.", reply_markup=keyboard_menu)

# Гибралтар
@dp.message_handler(lambda message: message.text.lower() == 'гибралтар' or message.text.lower() == 'gibraltar' or message.text.lower() == 'ub,hfknfh')
async def gibraltar_by_search(message: Message):
    command="Gibraltar"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gibraltar-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гибралтар.", reply_markup=keyboard_menu)

# Гондурас
@dp.message_handler(lambda message: message.text.lower() == 'гондурас' or message.text.lower() == 'honduras' or message.text.lower() == 'ujylehfc')
async def honduras_by_search(message: Message):
    command="Honduras"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gonduras-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гондурас.", reply_markup=keyboard_menu)

# Гонконг
@dp.message_handler(lambda message: message.text.lower() == 'гонконг' or message.text.lower() == 'hong kong' or message.text.lower() == 'ujyrjyu')
async def hong_kong_by_search(message: Message):
    command="Hong Kong"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gonkong-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гонконг.", reply_markup=keyboard_menu)

# Гренада
@dp.message_handler(lambda message: message.text.lower() == 'гренада' or message.text.lower() == 'grenada' or message.text.lower() == 'uhtyflf')
async def grenada_by_search(message: Message):
    command="Grenada"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Grenada-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гренаду.", reply_markup=keyboard_menu)

# ??? Гренландия
@dp.message_handler(lambda message: message.text.lower() == 'гренландия' or message.text.lower() == 'greenland' or message.text.lower() == 'uhtykfylbz')
async def greenland_by_search(message: Message):
    command="Greenland"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Grenlandiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гренландию.", reply_markup=keyboard_menu)

# Греция
@dp.message_handler(lambda message: message.text.lower() == 'греция' or message.text.lower() == 'greece' or message.text.lower() == 'uhtwbz')
async def greece_by_search(message: Message):
    command="Greece"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Greciya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Грецию.", reply_markup=keyboard_menu)

# Грузия
@dp.message_handler(lambda message: message.text.lower() == 'грузия' or message.text.lower() == 'georgia' or message.text.lower() == 'uhepbz')
async def georgia_by_search(message: Message):
    command="Georgia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Gruziya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Грузию.", reply_markup=keyboard_menu)

# Гуам
@dp.message_handler(lambda message: message.text.lower() == 'гуам' or message.text.lower() == 'guam' or message.text.lower() == 'uefv')
async def guam_by_search(message: Message):
    command="Guam"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Guam-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гуам.", reply_markup=keyboard_menu)

# Дания
@dp.message_handler(lambda message: message.text.lower() == 'дания' or message.text.lower() == 'denmark' or message.text.lower() == 'lfybz')
async def denmark_by_search(message: Message):
    command="Denmark"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Daniya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Данию.", reply_markup=keyboard_menu)

# Демократическая Республика Конго (Конго-Киншаса)
@dp.message_handler(lambda message: message.text.lower() == 'конго-киншаса' or message.text.lower() == 'демократическая республика конго' or message.text.lower() == 'конго киншаса' or message.text.lower() == 'congo kinshasa' or message.text.lower() == 'congo-kinshasa' or message.text.lower() == 'democratic republic of the congo' or message.text.lower() == 'democratic republic of congo' or message.text.lower() == 'ltvjrhfnbxtcrfz htcge,kbrf rjyuj' or message.text.lower() == 'rjyuj-rbyifcf' or message.text.lower() == 'rjyuj rbyifcf')
async def congo_kinshasa_by_search(message: Message):
    command="Congo-Kinshasa"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Demokraticheskaya-Respublika-Kongo-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Конго-Киншасу.", reply_markup=keyboard_menu)

# Джерси
@dp.message_handler(lambda message: message.text.lower() == 'джерси' or message.text.lower() == 'jersey' or message.text.lower() == 'l;thcb')
async def jersey_by_search(message: Message):
    command="Jersey"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Dzhersi-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Джерси.", reply_markup=keyboard_menu)

# Джибути
@dp.message_handler(lambda message: message.text.lower() == 'джибути' or message.text.lower() == 'djibouti' or message.text.lower() == 'l;b,enb')
async def djibouti_by_search(message: Message):
    command="Djibouti"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Dzhibuti-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Джибути.", reply_markup=keyboard_menu)

# Доминика
@dp.message_handler(lambda message: message.text.lower() == 'доминика' or message.text.lower() == 'dominica' or message.text.lower() == 'ljvbybrf')
async def dominica_by_search(message: Message):
    command="Dominica"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Dominika-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Доминику.", reply_markup=keyboard_menu)

# Доминикана
@dp.message_handler(lambda message: message.text.lower() == 'доминикана' or message.text.lower() == 'dominican republic' or message.text.lower() == 'ljvbybrfyf')
async def dominican_republic_by_search(message: Message):
    command="Dominican Republic"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Dominikana-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Доминикану.", reply_markup=keyboard_menu)

# Египет
@dp.message_handler(lambda message: message.text.lower() == 'египет' or message.text.lower() == 'egypt' or message.text.lower() == 'tubgtn')
async def egypt_by_search(message: Message):
    command="Egypt"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Egipet-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Египет.", reply_markup=keyboard_menu)

# Замбия
@dp.message_handler(lambda message: message.text.lower() == 'замбия' or message.text.lower() == 'zambia' or message.text.lower() == 'pfv,bz')
async def zambia_by_search(message: Message):
    command="Zambia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Zambiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Замбию.", reply_markup=keyboard_menu)

# Западное Самоа
@dp.message_handler(lambda message: message.text.lower() == 'западное самоа' or message.text.lower() == 'west samoa' or message.text.lower() == 'pfgflyjt cfvjf')
async def west_samoa_by_search(message: Message):
    command="West Samoa"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Zapadnoe-Samoa-Samoa-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Западное Самоа.", reply_markup=keyboard_menu)

# Зимбабве
@dp.message_handler(lambda message: message.text.lower() == 'зимбабве' or message.text.lower() == 'zimbabwe' or message.text.lower() == 'pbv,f,dt')
async def zimbabwe_by_search(message: Message):
    command="Zimbabwe"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Zimbabve-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Зимбабве.", reply_markup=keyboard_menu)

# Израиль
@dp.message_handler(lambda message: message.text.lower() == 'израиль' or message.text.lower() == 'israel' or message.text.lower() == 'bphfbkm')
async def israel_by_search(message: Message):
    command="Israel"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Izrail-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Израиль.", reply_markup=keyboard_menu)

# Индия
@dp.message_handler(lambda message: message.text.lower() == 'индия' or message.text.lower() == 'india' or message.text.lower() == 'bylbz')
async def india_by_search(message: Message):
    command="India"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Indiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Индию.", reply_markup=keyboard_menu)

# Индонезия
@dp.message_handler(lambda message: message.text.lower() == 'индонезия' or message.text.lower() == 'indonesia' or message.text.lower() == 'byljytpbz')
async def indonesia_by_search(message: Message):
    command="Indonesia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Indoneziya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Индонезию.", reply_markup=keyboard_menu)

# Иордания
@dp.message_handler(lambda message: message.text.lower() == 'иордания' or message.text.lower() == 'jordan' or message.text.lower() == 'bjhlfybz')
async def jordan_by_search(message: Message):
    command="Jordan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Iordaniya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Иорданию.", reply_markup=keyboard_menu)

# Ирак
@dp.message_handler(lambda message: message.text.lower() == 'ирак' or message.text.lower() == 'iraq' or message.text.lower() == 'bhfr')
async def iraq_by_search(message: Message):
    command="Iraq"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Irak-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ирак.", reply_markup=keyboard_menu)

# Иран
@dp.message_handler(lambda message: message.text.lower() == 'иран' or message.text.lower() == 'iran' or message.text.lower() == 'bhfy')
async def iran_by_search(message: Message):
    command="Iran"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Iran-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Иран.", reply_markup=keyboard_menu)

# Ирландия
@dp.message_handler(lambda message: message.text.lower() == 'ирландия' or message.text.lower() == 'ireland' or message.text.lower() == 'bhkfylbz')
async def ireland_by_search(message: Message):
    command="Ireland"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Irlandiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ирландию.", reply_markup=keyboard_menu)

# Исландия
@dp.message_handler(lambda message: message.text.lower() == 'исландия' or message.text.lower() == 'iceland' or message.text.lower() == 'bckfylbz')
async def iceland_by_search(message: Message):
    command="Iceland"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Islandiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Исландию.", reply_markup=keyboard_menu)

# Испания
@dp.message_handler(lambda message: message.text.lower() == 'испания' or message.text.lower() == 'spain' or message.text.lower() == 'bcgfybz')
async def spain_by_search(message: Message):
    command="Spain"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ispaniya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Испанию.", reply_markup=keyboard_menu)

# Италия
@dp.message_handler(lambda message: message.text.lower() == 'италия' or message.text.lower() == 'italy' or message.text.lower() == 'bnfkbz')
async def italy_by_search(message: Message):
    command="Italy"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Italiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Италию.", reply_markup=keyboard_menu)

# Йемен
@dp.message_handler(lambda message: message.text.lower() == 'йемен' or message.text.lower() == 'yemen' or message.text.lower() == 'qtvty')
async def yemen_by_search(message: Message):
    command="Yemen"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Jemen-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Йемен.", reply_markup=keyboard_menu)

# Кабо-Верде
@dp.message_handler(lambda message: message.text.lower() == 'кабо-верде' or message.text.lower() == 'кабо верде' or message.text.lower() == 'кабо' or message.text.lower() == 'верде' or message.text.lower() == 'cape verde' or message.text.lower() == 'cape' or message.text.lower() == 'verde' or message.text.lower() == 'rf,j-dthlt' or message.text.lower() == 'rf,j dthlt' or message.text.lower() == 'rf,j' or message.text.lower() == 'dthlt')
async def cape_verde_by_search(message: Message): 
    command="Cape Verde"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kabo-Verde-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Кабо-Верде.", reply_markup=keyboard_menu)

# Казахстан
@dp.message_handler(lambda message: message.text.lower() == 'казахстан' or message.text.lower() == 'kazakhstan' or message.text.lower() == 'rfpf[cnfy')
async def kazakhstan_by_search(message: Message): 
    command="Kazakhstan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kazahstan-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Казахстан.", reply_markup=keyboard_menu)

# Каймановы острова (острова Кайман)
@dp.message_handler(lambda message: message.text.lower() == 'каймановы острова' or message.text.lower() == 'острова кайман' or message.text.lower() == 'каймановы' or message.text.lower() == 'кайман' or message.text.lower() == 'cayman islands' or message.text.lower() == 'cayman' or message.text.lower() == 'rfqvfyjds jcnhjdf' or message.text.lower() == 'rfqvfyjds' or message.text.lower() == 'rfqvfy' or message.text.lower() == 'jcnhjdf rfqvfy')
async def cayman_islands_by_search(message: Message): 
    command="Cayman islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kajmanovy-ostrova-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Каймановы острова.", reply_markup=keyboard_menu)

# Камбоджа
@dp.message_handler(lambda message: message.text.lower() == 'камбоджа' or message.text.lower() == 'cambodia' or message.text.lower() == 'rfv,jl;f')
async def cambodia_by_search(message: Message): 
    command="Cambodia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kambodzha-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Камбоджу.", reply_markup=keyboard_menu)

# Камерун
@dp.message_handler(lambda message: message.text.lower() == 'камерун' or message.text.lower() == 'cameroon' or message.text.lower() == 'rfvthey')
async def cameroon_by_search(message: Message): 
    command="Cameroon"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kamerun-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Камерун.", reply_markup=keyboard_menu)

# Канада
@dp.message_handler(lambda message: message.text.lower() == 'канада' or message.text.lower() == 'canada' or message.text.lower() == 'rfyflf')
async def canada_by_search(message: Message): 
    command="Canada"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kanada-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Канаду.", reply_markup=keyboard_menu)

# Катар
@dp.message_handler(lambda message: message.text.lower() == 'катар' or message.text.lower() == 'qatar' or message.text.lower() == 'rfnfh')
async def qatar_by_search(message: Message): 
    command="Qatar"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Katar-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Катар.", reply_markup=keyboard_menu)

# Кения
@dp.message_handler(lambda message: message.text.lower() == 'кения' or message.text.lower() == 'kenya' or message.text.lower() == 'rtybz')
async def kenya_by_search(message: Message): 
    command="Kenya"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Keniya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Кению.", reply_markup=keyboard_menu)

# Кипр
@dp.message_handler(lambda message: message.text.lower() == 'кипр' or message.text.lower() == 'cyprus' or message.text.lower() == 'rbgh')
async def cyprus_by_search(message: Message): 
    command="Cyprus"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kipr-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Кипр.", reply_markup=keyboard_menu)

# Кыргызстан
@dp.message_handler(lambda message: message.text.lower() == 'кыргызстан' or message.text.lower() == 'киргизия' or message.text.lower() == 'kyrgyzstan' or message.text.lower() == 'rbhubpbz' or message.text.lower() == 'rshuspcnfy')
async def kyrgyzstan_by_search(message: Message): 
    command="Kyrgyzstan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kirgiziya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Кыргызстан.", reply_markup=keyboard_menu)

# Кирибати
@dp.message_handler(lambda message: message.text.lower() == 'кирибати' or message.text.lower() == 'kiribati' or message.text.lower() == 'rbhb,fnb')
async def kiribati_by_search(message: Message): 
    command="Kiribati"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kiribati-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Кирибати.", reply_markup=keyboard_menu)

# Китай
@dp.message_handler(lambda message: message.text.lower() == 'китай' or message.text.lower() == 'кнр' or message.text.lower() == 'china' or message.text.lower() == 'ryh' or message.text.lower() == 'rbnfq')
async def china_by_search(message: Message): 
    command="China"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kitaj-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Китай.", reply_markup=keyboard_menu)

# КНДР (Северная Корея)
@dp.message_handler(lambda message: message.text.lower() == 'северная корея' or message.text.lower() == 'кндр' or message.text.lower() == 'north korea' or message.text.lower() == 'rylh' or message.text.lower() == 'ctdthyfz rjhtz')
async def north_korea_by_search(message: Message): 
    command="North Korea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/KNDR-Severnaya-Koreya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Северную Корею.", reply_markup=keyboard_menu)

# Колумбия
@dp.message_handler(lambda message: message.text.lower() == 'колумбия' or message.text.lower() == 'colombia' or message.text.lower() == 'rjkev,bz')
async def colombia_by_search(message: Message): 
    command="Colombia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kolumbiya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Колумбию.", reply_markup=keyboard_menu)

"""
# Кокосовые острова
@dp.message_handler(lambda message: message.text.lower() == 'кокосовые острова' or message.text.lower() == 'cocos islands' or message.text.lower() == 'rjrjcjdst jcnhjdf')
async def cocos_islands_by_search(message: Message): 
    command="Cocos islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kokosovye-ostrova-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Кокосовые острова.", reply_markup=keyboard_menu)
"""

# Коморские острова
@dp.message_handler(lambda message: message.text.lower() == 'коморские острова' or message.text.lower() == 'коморские' or message.text.lower() == 'comoros' or message.text.lower() == 'rjvjhcrbt' or message.text.lower() == 'rjvjhcrbt jcnhjdf')
async def comoros_by_search(message: Message): 
    command="Comoros"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Komorskie-ostrova-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Коморские острова.", reply_markup=keyboard_menu)

# Республика Конго (Конго-Браззавиль)
@dp.message_handler(lambda message: message.text.lower() == 'республика конго' or message.text.lower() == 'конго браззавиль' or message.text.lower() == 'конго-браззавиль' or message.text.lower() == 'congo brazzaville' or message.text.lower() == 'congo-brazzaville' or message.text.lower() == 'republic of the congo' or message.text.lower() == 'republic of congo' or message.text.lower() == 'rjyuj-,hfppfdbkm' or message.text.lower() == 'rjyuj ,hfppfdbkm' or message.text.lower() == 'htcge,kbrf rjyuj')
async def solomon_islands_by_search(message: Message): 
    command="Solomon islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Respublika-Kongo-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Республику Конго.", reply_markup=keyboard_menu)

# Корея (Южная Корея)
@dp.message_handler(lambda message: message.text.lower() == 'южная корея' or message.text.lower() == 'south korea' or message.text.lower() == '.;yfz rjhtz')
async def south_korea_by_search(message: Message): 
    command="South Korea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/YUzhnaya-Koreya-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Южную Корею.", reply_markup=keyboard_menu)

# Коста-Рика
@dp.message_handler(lambda message: message.text.lower() == 'коста-рика' or message.text.lower() == 'коста рика' or message.text.lower() == 'costa rica' or message.text.lower() == 'rjcnf-hbrf' or message.text.lower() == 'rjcnf hbrf')
async def costa_rica_by_search(message: Message): 
    command="Costa Rica"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kosta-Rika-poehali-04-30')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Коста-Рику.", reply_markup=keyboard_menu)

# Кот-д’Ивуар
@dp.message_handler(lambda message: message.text.lower() == 'кот-д’ивуар' or message.text.lower() == 'котдивуар' or message.text.lower() == 'кот дивуар' or message.text.lower() == 'кот-дивуар' or message.text.lower() == 'ivory coast' or message.text.lower() == 'rjn-l\'bdefh' or message.text.lower() == 'rjnlbdefh' or message.text.lower() == 'rjn-lbdefh' or message.text.lower() == 'rjn lbdefh')
async def ivory_coast_by_search(message: Message): 
    command="Ivory Coast"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kot-dIvuar-poehali-05-01')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Кот-д’Ивуар.", reply_markup=keyboard_menu)

# Куба
@dp.message_handler(lambda message: message.text.lower() == 'куба' or message.text.lower() == 'cuba' or message.text.lower() == 're,f')
async def cuba_by_search(message: Message): 
    command="Cuba"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kuba-poehali-05-01')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Кубу.", reply_markup=keyboard_menu)

# Кувейт
@dp.message_handler(lambda message: message.text.lower() == 'кувейт' or message.text.lower() == 'kuwait' or message.text.lower() == 'redtqn')
async def kuwait_by_search(message: Message): 
    command="Kuwait"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kuvejt-poehali-05-01')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Кувейт.", reply_markup=keyboard_menu)

# Кюрасао
@dp.message_handler(lambda message: message.text.lower() == 'кюрасао' or message.text.lower() == 'curacao' or message.text.lower() == 'r.hfcfj')
async def curacao_by_search(message: Message): 
    command="Curacao"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Kyurasao-poehali-05-01')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Кюрасао.", reply_markup=keyboard_menu)

# Лаос
@dp.message_handler(lambda message: message.text.lower() == 'лаос' or message.text.lower() == 'laos' or message.text.lower() == 'kfjc')
async def laos_by_search(message: Message):
    command="Laos"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Laos-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Лаос.", reply_markup=keyboard_menu)

# Латвия
@dp.message_handler(lambda message: message.text.lower() == 'латвия' or message.text.lower() == 'latvia' or message.text.lower() == 'kfndbz')
async def latvia_by_search(message: Message):
    command="Latvia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Latviya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Латвию.", reply_markup=keyboard_menu)

# Лесото
@dp.message_handler(lambda message: message.text.lower() == 'лесото' or message.text.lower() == 'lesotho' or message.text.lower() == 'ktcjnj')
async def lesotho_by_search(message: Message):
    command="Lesotho"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Lesoto-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Лесото.", reply_markup=keyboard_menu)

# Либерия
@dp.message_handler(lambda message: message.text.lower() == 'либерия' or message.text.lower() == 'liberia' or message.text.lower() == 'kb,thbz')
async def liberia_by_search(message: Message):
    command="Liberia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Liberiya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Либерию.", reply_markup=keyboard_menu)

# Ливан
@dp.message_handler(lambda message: message.text.lower() == 'ливан' or message.text.lower() == 'lebanon' or message.text.lower() == 'kbdfy')
async def lebanon_by_search(message: Message):
    command="Lebanon"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Livan-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ливан.", reply_markup=keyboard_menu)

# Ливия
@dp.message_handler(lambda message: message.text.lower() == 'ливия' or message.text.lower() == 'libya' or message.text.lower() == 'kbdbz')
async def libya_by_search(message: Message):
    command="Libya"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Liviya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ливию.", reply_markup=keyboard_menu)

# Литва
@dp.message_handler(lambda message: message.text.lower() == 'литва' or message.text.lower() == 'lithuania' or message.text.lower() == 'kbndf')
async def lithuania_by_search(message: Message):
    command="Lithuania"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Litva-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Литву.", reply_markup=keyboard_menu)

# Лихтенштейн
@dp.message_handler(lambda message: message.text.lower() == 'лихтенштейн' or message.text.lower() == 'liechtenstein' or message.text.lower() == 'kb[ntyintqy')
async def liechtenstein_by_search(message: Message):
    command="Liechtenstein"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Lihtenshtejn-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Лихтенштейн.", reply_markup=keyboard_menu)

# Люксембург
@dp.message_handler(lambda message: message.text.lower() == 'люксембург' or message.text.lower() == 'luxemburg' or message.text.lower() == 'k.rctv,ehu')
async def luxemburg_by_search(message: Message):
    command="Luxemburg"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Lyuksemburg-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Люксембург.", reply_markup=keyboard_menu)

# Маврикий
@dp.message_handler(lambda message: message.text.lower() == 'маврикий' or message.text.lower() == 'mauritius' or message.text.lower() == 'vfdhbrbq')
async def mauritius_by_search(message: Message): 
    command="Mauritius"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Mavrikij-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Маврикий.", reply_markup=keyboard_menu)

# Мавритания
@dp.message_handler(lambda message: message.text.lower() == 'мавритания' or message.text.lower() == 'mauritania' or message.text.lower() == 'vfdhbnfybz')
async def mauritania_by_search(message: Message): 
    command="Mauritania"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Mavritaniya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Мавританию.", reply_markup=keyboard_menu)

# Мадагаскар
@dp.message_handler(lambda message: message.text.lower() == 'мадагаскар' or message.text.lower() == 'madagascar' or message.text.lower() == 'vflfufcrfh')
async def madagascar_by_search(message: Message): 
    command="Madagascar"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Madagaskar-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Мадагаскар.", reply_markup=keyboard_menu)

# Макао
@dp.message_handler(lambda message: message.text.lower() == 'макао' or message.text.lower() == 'macau' or message.text.lower() == 'vfrfj')
async def macau_by_search(message: Message): 
    command="Macau"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Makao-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Макао.", reply_markup=keyboard_menu)

# Македония (Северная Македония)
@dp.message_handler(lambda message: message.text.lower() == 'македония' or message.text.lower() == 'северная македония' or message.text.lower() == 'macedonia' or message.text.lower() == 'northern macedonia' or message.text.lower() == 'ctdthyfz vfrtljybz' or message.text.lower() == 'vfrtljybz')
async def northern_macedonia_by_search(message: Message): 
    command="Northern Macedonia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Severnaya-Makedoniya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Северную Македонию.", reply_markup=keyboard_menu)

# Малави
@dp.message_handler(lambda message: message.text.lower() == 'малави' or message.text.lower() == 'malawi' or message.text.lower() == 'vfkfdb')
async def malawi_by_search(message: Message): 
    command="Malawi"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Malavi-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Малави.", reply_markup=keyboard_menu)

# Малайзия
@dp.message_handler(lambda message: message.text.lower() == 'малайзия' or message.text.lower() == 'malaysia' or message.text.lower() == 'vfkfqpbz')
async def malaysia_by_search(message: Message): 
    command="Malaysia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Malajziya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Малайзию.", reply_markup=keyboard_menu)

# Мали
@dp.message_handler(lambda message: message.text.lower() == 'мали' or message.text.lower() == 'mali' or message.text.lower() == 'vfkb')
async def mali_by_search(message: Message): 
    command="Mali"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Mali-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Мали.", reply_markup=keyboard_menu)

# Мальдивы
@dp.message_handler(lambda message: message.text.lower() == 'мальдивы' or message.text.lower() == 'maldives' or message.text.lower() == 'vfkmlbds')
async def maldives_by_search(message: Message): 
    command="Maldives"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Maldivy-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Мальдивы.", reply_markup=keyboard_menu)

# Мальта
@dp.message_handler(lambda message: message.text.lower() == 'мальта' or message.text.lower() == 'malta' or message.text.lower() == 'vfkmnf')
async def malta_by_search(message: Message): 
    command="Malta"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Malta-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Мальту.", reply_markup=keyboard_menu)

# Марокко
@dp.message_handler(lambda message: message.text.lower() == 'марокко' or message.text.lower() == 'morocco' or message.text.lower() == 'vfhjrrj')
async def morocco_by_search(message: Message): 
    command="Morocco"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Marokko-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Марокко.", reply_markup=keyboard_menu)

"""
# Мартиника
@dp.message_handler(lambda message: message.text.lower() == 'мартиника' or message.text.lower() == 'martinique' or message.text.lower() == 'vfhnbybrf')
async def martinique_by_search(message: Message): 
    command="Martinique"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Martinika-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Мартинику.", reply_markup=keyboard_menu)
"""

# Маршалловы острова
@dp.message_handler(lambda message: message.text.lower() == 'маршалловы острова' or message.text.lower() == 'маршалловы' or message.text.lower() == 'marshall islands' or message.text.lower() == 'marshall' or message.text.lower() == 'vfhifkkjds' or message.text.lower() == 'vfhifkkjds jcnhjdf')
async def marshall_islands_by_search(message: Message): 
    command="Marshall islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Marshallovy-ostrova-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Маршалловы острова.", reply_markup=keyboard_menu)

# Мексика
@dp.message_handler(lambda message: message.text.lower() == 'мексика' or message.text.lower() == 'mexico' or message.text.lower() == 'vtrcbrf')
async def mexico_by_search(message: Message): 
    command="Mexico"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Meksika-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Мексику.", reply_markup=keyboard_menu)

# Микронезия
@dp.message_handler(lambda message: message.text.lower() == 'микронезия' or message.text.lower() == 'micronesia' or message.text.lower() == 'vbrhjytpbz')
async def micronesia_by_search(message: Message): 
    command="Micronesia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Mikroneziya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Микронезию.", reply_markup=keyboard_menu)

# Мозамбик
@dp.message_handler(lambda message: message.text.lower() == 'мозамбик' or message.text.lower() == 'mozambique' or message.text.lower() == 'vjpfv,br')
async def mozambique_by_search(message: Message): 
    command="Mozambique"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Mozambik-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Мозамбик.", reply_markup=keyboard_menu)

# Молдавия (Молдова)
@dp.message_handler(lambda message: message.text.lower() == 'молдавия' or message.text.lower() == 'молдова' or message.text.lower() == 'moldova' or message.text.lower() == 'vjkljdf' or message.text.lower() == 'vjklfdbz')
async def moldova_by_search(message: Message): 
    command="Ьoldova"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Moldaviya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Молдову.", reply_markup=keyboard_menu)

# Монако
@dp.message_handler(lambda message: message.text.lower() == 'монако' or message.text.lower() == 'monaco' or message.text.lower() == 'vjyfrj')
async def monaco_by_search(message: Message): 
    command="Monaco"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Monako-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Монако.", reply_markup=keyboard_menu)

# Монголия
@dp.message_handler(lambda message: message.text.lower() == 'монголия' or message.text.lower() == 'mongolia' or message.text.lower() == 'vjyujkbz')
async def mongolia_by_search(message: Message): 
    command="Mongolia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Mongoliya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Монголию.", reply_markup=keyboard_menu)

# Монтсеррат
@dp.message_handler(lambda message: message.text.lower() == 'монтсеррат' or message.text.lower() == 'montserrat' or message.text.lower() == 'vjyncthhfn')
async def montserrat_by_search(message: Message): 
    command="Montserrat"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Montserrat-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Монтсеррат.", reply_markup=keyboard_menu)

# Мьянма
@dp.message_handler(lambda message: message.text.lower() == 'мьянма' or message.text.lower() == 'myanmar' or message.text.lower() == 'vmzyvf')
async def myanmar_by_search(message: Message): 
    command="Myanmar"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Myanma-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Мьянму.", reply_markup=keyboard_menu)

# Намибия
@dp.message_handler(lambda message: message.text.lower() == 'намибия' or message.text.lower() == 'namibia' or message.text.lower() == 'yfvb,bz')
async def namibia_by_search(message: Message): 
    command="Namibia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Namibiya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Намибию.", reply_markup=keyboard_menu)

"""
# Народная Республика Конго
@dp.message_handler(lambda message: message.text.lower() == 'народная республика конго' or message.text.lower() == 'national republic of congo' or message.text.lower() == 'national republic of the congo' or message.text.lower() == 'yfhjlyfz htcge,kbrf rjyuj')
async def national_republic_of_the_congo_by_search(message: Message): 
    command="National Republic of the Congo"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Narodnaya-Respublika-Kongo-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Народную Республику Конго.", reply_markup=keyboard_menu)
"""

# Науру
@dp.message_handler(lambda message: message.text.lower() == 'науру' or message.text.lower() == 'nauru' or message.text.lower() == 'yfehe')
async def nauru_by_search(message: Message): 
    command="Nauru"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Nauru-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Науру.", reply_markup=keyboard_menu)

# Непал
@dp.message_handler(lambda message: message.text.lower() == 'непал' or message.text.lower() == 'nepal' or message.text.lower() == 'ytgfk')
async def nepal_by_search(message: Message): 
    command="Nepal"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Nepal-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Непал.", reply_markup=keyboard_menu)

# Нигер
@dp.message_handler(lambda message: message.text.lower() == 'нигер' or message.text.lower() == 'niger' or message.text.lower() == 'ybuth')
async def niger_by_search(message: Message): 
    command="Niger"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Niger-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Нигер.", reply_markup=keyboard_menu)

# Нигерия
@dp.message_handler(lambda message: message.text.lower() == 'нигерия' or message.text.lower() == 'nigeria' or message.text.lower() == 'ybuthbz')
async def nigeria_by_search(message: Message): 
    command="Nigeria"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Nigeriya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Нигерию.", reply_markup=keyboard_menu)

# Нидерланды
@dp.message_handler(lambda message: message.text.lower() == 'нидерланды' or message.text.lower() == 'netherlands' or message.text.lower() == 'yblthkfyls')
async def netherlands_by_search(message: Message): 
    command="Netherlands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Niderlandy-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Нидерланды.", reply_markup=keyboard_menu)

# Никарагуа
@dp.message_handler(lambda message: message.text.lower() == 'никарагуа' or message.text.lower() == 'nicaragua' or message.text.lower() == 'ybrfhfuef')
async def nicaragua_by_search(message: Message): 
    command="Nicaragua"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Nikaragua-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Никарагуа.", reply_markup=keyboard_menu)

# Ниуэ
@dp.message_handler(lambda message: message.text.lower() == 'ниуэ' or message.text.lower() == 'niue' or message.text.lower() == 'ybe\'')
async def niue_by_search(message: Message): 
    command="Niue"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Niueh-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ниуэ.", reply_markup=keyboard_menu)

# Новая Зеландия
@dp.message_handler(lambda message: message.text.lower() == 'новая зеландия' or message.text.lower() == 'new zealand' or message.text.lower() == 'yjdfz ptkfylbz')
async def new_zealand_by_search(message: Message): 
    command="New Zealand"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Novaya-Zelandiya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Новую Зеландию.", reply_markup=keyboard_menu)

# Новая Каледония
@dp.message_handler(lambda message: message.text.lower() == 'новая каледония' or message.text.lower() == 'new caledonia' or message.text.lower() == 'yjdfz rfktljybz')
async def new_caledonia_by_search(message: Message): 
    command="New Caledonia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Novaya-Kaledoniya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Новую Каледонию.", reply_markup=keyboard_menu)

# Норвегия
@dp.message_handler(lambda message: message.text.lower() == 'норвегия' or message.text.lower() == 'norway' or message.text.lower() == 'yjhdtubz')
async def norway_by_search(message: Message): 
    command="Norway"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Norvegiya-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Норвегию.", reply_markup=keyboard_menu)

# ОАЭ (Эмираты)
@dp.message_handler(lambda message: message.text.lower() == 'оаэ' or message.text.lower() == 'эмираты' or message.text.lower() == 'объединённые арабские эмираты' or message.text.lower() == 'объединенные арабские эмираты' or message.text.lower() == 'united arab emirates' or message.text.lower() == 'uae' or message.text.lower() == 'jf\'' or message.text.lower() == '\'vbhfns' or message.text.lower() == 'j,]tlbytyyst fhf,crbt \'vbhfns')
async def united_arab_emirates_by_search(message: Message): 
    command="United Arab Emirates"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/OAEH-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в ОАЭ.", reply_markup=keyboard_menu)

# Оман
@dp.message_handler(lambda message: message.text.lower() == 'оман' or message.text.lower() == 'oman' or message.text.lower() == 'jvfy')
async def oman_by_search(message: Message): 
    command="Oman"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Oman-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Оман.", reply_markup=keyboard_menu)

# Остров Бонайре (Бонайре)
@dp.message_handler(lambda message: message.text.lower() == 'остров бонайре' or message.text.lower() == 'бонайре' or message.text.lower() == 'bonaira' or message.text.lower() == 'bonaira island' or message.text.lower() == 'jcnhjd ,jyfqht' or message.text.lower() == ',jyfqht')
async def bonaira_island_by_search(message: Message): 
    command="Bonaira island"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrov-Bonajre-poehali-04-27')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на остров Бонайре.", reply_markup=keyboard_menu)

# Острова Кука
@dp.message_handler(lambda message: message.text.lower() == 'острова кука' or message.text.lower() == 'cook islands' or message.text.lower() == 'jcnhjdf rerf')
async def cook_islands_by_search(message: Message): 
    command="Сook islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrova-Kuka-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на острова Кука.", reply_markup=keyboard_menu)

# Острова Норфолк
@dp.message_handler(lambda message: message.text.lower() == 'острова норфолк' or message.text.lower() == 'норфолк' or message.text.lower() == 'norfolk islands' or message.text.lower() == 'norfolk' or message.text.lower() == 'yjhajkr' or message.text.lower() == 'jcnhjdf yjhajkr')
async def norfolk_islands_by_search(message: Message): 
    command="Тorfolk islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Norfolk-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на острова Норфолк.", reply_markup=keyboard_menu)

# Остров Саба
@dp.message_handler(lambda message: message.text.lower() == 'остров саба' or message.text.lower() == 'саба' or message.text.lower() == 'saba island' or message.text.lower() == 'saba' or message.text.lower() == 'cf,f' or message.text.lower() == 'jcnhjd cf,f')
async def saba_island_by_search(message: Message): 
    command="Saba island"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrov-Saba-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на остров Саба.", reply_markup=keyboard_menu)

# Остров Святой Елены
@dp.message_handler(lambda message: message.text.lower() == 'остров святой елены' or message.text.lower() == 'st. helena island' or message.text.lower() == 'st helena island' or message.text.lower() == 'saint helena island' or message.text.lower() == 'jcnhjd cdznjq tktys')
async def st_helena_island_by_search(message: Message): 
    command="St. Helena island"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrov-Svyatoj-Eleny-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на остров Святой Елены.", reply_markup=keyboard_menu)

"""
# Остров Сен-Бартелеми (Сен-Бартелеми)
@dp.message_handler(lambda message: message.text.lower() == 'остров сен-бартелеми' or message.text.lower() == 'сен бартелеми' or message.text.lower() == 'сен-бартелеми' or message.text.lower() == 'saint-bartelemi island' or message.text.lower() == 'saint-bartelemi' or message.text.lower() == 'saint bartelemi' or message.text.lower() == 'st bartelemi' or message.text.lower() == 'cty ,fhntktvb' or message.text.lower() == 'cty-,fhntktvb' or message.text.lower() == 'jcnhjd cty-,fhntktvb')
async def saint_bartelemi_island_by_search(message: Message): 
    command="Saint-Bartelemi island"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrov-Sen-Bartelemi-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на остров Сен-Бартелеми.", reply_markup=keyboard_menu)
"""

# Остров Сен-Мартен (Сен-Мартен)
@dp.message_handler(lambda message: message.text.lower() == 'остров сен-мартен' or message.text.lower() == 'сен-мартен' or message.text.lower() == 'сен мартен' or message.text.lower() == 'saint-martin island' or message.text.lower() == 'saint-martin' or message.text.lower() == 'st martin' or message.text.lower() == 'st. martin' or message.text.lower() == 'saint martin' or message.text.lower() == 'jcnhjd cty-vfhnty' or message.text.lower() == 'cty-vfhnty' or message.text.lower() == 'cty vfhnty')
async def saint_martin_island_by_search(message: Message): 
    command="Saint-Martin island"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrov-Sen-Marten-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на остров Сен-Мартен.", reply_markup=keyboard_menu)

# Остров Синт-Эстатиус (Синт-Эстатиус)
@dp.message_handler(lambda message: message.text.lower() == 'остров синт-эстатиус' or message.text.lower() == 'синт-эстатиус' or message.text.lower() == 'синт эстатиус' or message.text.lower() == 'sint estatius island' or message.text.lower() == 'sint estatius' or message.text.lower() == 'sint-estatius' or message.text.lower() == 'jcnhjd cbyn-\'cnfnbec' or message.text.lower() == 'cbyn-\'cnfnbec' or message.text.lower() == 'cbyn \'cnfnbec')
async def sint_estatius_island_by_search(message: Message): 
    command="Sint Estatius island"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrov-Sint-EHstatius-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на остров Синт-Эстатиус.", reply_markup=keyboard_menu)

"""
# Острова Уоллис и Футуна
@dp.message_handler(lambda message: message.text.lower() == 'острова уоллис и футуна' or message.text.lower() == 'уоллис и футуна' or message.text.lower() == 'wallis and futuna islands' or message.text.lower() == 'wallis and futuna' or message.text.lower() == 'jcnhjdf ejkkbc b aeneyf' or message.text.lower() == 'ejkkbc b aeneyf')
async def wallis_and_futuna_islands_by_search(message: Message): 
    command="Wallis and Futuna islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrova-Uollis-i-Futuna-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на острова Уоллис и Футуна.", reply_markup=keyboard_menu)
"""

"""
# Острова Херд и МакДональд
@dp.message_handler(lambda message: message.text.lower() == 'острова херд и макдональд' or message.text.lower() == 'херд и макдональд' or message.text.lower() == 'herd and macdonald islands' or message.text.lower() == 'herd and macdonald' or message.text.lower() == 'jcnhjdf [thl b vfrljyfkl]' or message.text.lower() == '[thl b vfrljyfkl]')
async def herd_and_macdonald_islands_by_search(message: Message): 
    command="Herd and MacDonald islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ostrova-Herd-i-MakDonald-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на острова Херд и МакДональд.", reply_markup=keyboard_menu)
"""

# Пакистан
@dp.message_handler(lambda message: message.text.lower() == 'пакистан' or message.text.lower() == 'pakistan' or message.text.lower() == 'gfrbcnfy')
async def pakistan_by_search(message: Message): 
    command="Pakistan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Pakistan-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Пакистан.", reply_markup=keyboard_menu)

# Палау
@dp.message_handler(lambda message: message.text.lower() == 'палау' or message.text.lower() == 'palau' or message.text.lower() == 'gfkfe')
async def palau_by_search(message: Message): 
    command="Palau"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Palau-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Палау.", reply_markup=keyboard_menu)

"""
# Палестина
@dp.message_handler(lambda message: message.text.lower() == 'палестина' or message.text.lower() == 'palestine' or message.text.lower() == 'gfktcnbyf')
async def palestine_by_search(message: Message): 
    command="Palestine"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Palestina-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Палестину.", reply_markup=keyboard_menu)
"""

# Панама
@dp.message_handler(lambda message: message.text.lower() == 'панама' or message.text.lower() == 'panama' or message.text.lower() == 'gfyfvf')
async def panama_by_search(message: Message): 
    command="Panama"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Panama-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Панаму.", reply_markup=keyboard_menu)

# Папуа-Новая Гвинея
@dp.message_handler(lambda message: message.text.lower() == 'папуа-новая гвинея' or message.text.lower() == 'папуа новая гвинея' or message.text.lower() == 'папуа' or message.text.lower() == 'новая гвинея' or message.text.lower() == 'papua' or message.text.lower() == 'new guinea' or message.text.lower() == 'papua new guinea' or message.text.lower() == 'papua-new guinea' or message.text.lower() == 'gfgef-yjdfz udbytz' or message.text.lower() == 'gfgef yjdfz udbytz' or message.text.lower() == 'yjdfz udbytz' or message.text.lower() == 'gfgef')
async def papua_new_guinea_by_search(message: Message): 
    command="Papua new Guinea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Papua-Novaya-Gvineya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Папуа-Новую Гвинею.", reply_markup=keyboard_menu)

# Парагвай
@dp.message_handler(lambda message: message.text.lower() == 'парагвай' or message.text.lower() == 'paraguay' or message.text.lower() == 'gfhfudfq')
async def paraguay_by_search(message: Message): 
    command="Paraguay"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Paragvaj-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Парагвай.", reply_markup=keyboard_menu)

# Перу
@dp.message_handler(lambda message: message.text.lower() == 'перу' or message.text.lower() == 'peru' or message.text.lower() == 'gthe')
async def peru_by_search(message: Message): 
    command="Peru"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Peru-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Перу.", reply_markup=keyboard_menu)

# Польша
@dp.message_handler(lambda message: message.text.lower() == 'польша' or message.text.lower() == 'poland' or message.text.lower() == 'gjkmif')
async def poland_by_search(message: Message): 
    command="Poland"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Polsha-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Польшу.", reply_markup=keyboard_menu)

# Португалия
@dp.message_handler(lambda message: message.text.lower() == 'португалия' or message.text.lower() == 'portugal' or message.text.lower() == 'gjhneufkbz')
async def portugal_by_search(message: Message): 
    command="Portugal"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Portugaliya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Португалию.", reply_markup=keyboard_menu)

# Пуэрто-Рико
@dp.message_handler(lambda message: message.text.lower() == 'пуэрто-рико' or message.text.lower() == 'пуэрто рико' or message.text.lower() == 'puerto rico' or message.text.lower() == 'puerto-rico' or message.text.lower() == 'ge\'hnj hbrj' or message.text.lower() == 'ge\'hnj-hbrj')
async def puerto_rico_by_search(message: Message): 
    command="Puerto Rico"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Puehrto-Riko-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Пуэрто-Рико.", reply_markup=keyboard_menu)

# Реюньон
@dp.message_handler(lambda message: message.text.lower() == 'реюньон' or message.text.lower() == 'reunion' or message.text.lower() == 'ht.ymjy')
async def reunion_by_search(message: Message):
    command="Reunion"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Reyunon-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Реюньон.", reply_markup=keyboard_menu)

"""
# Россия
@dp.message_handler(lambda message: message.text.lower() == 'россия' or message.text.lower() == 'russia' or message.text.lower() == 'hjccbz')
async def russia_by_search(message: Message):
    command="Russia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Rossiya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Россию.", reply_markup=keyboard_menu)
"""

# Руанда
@dp.message_handler(lambda message: message.text.lower() == 'руанда' or message.text.lower() == 'rwanda' or message.text.lower() == 'hefylf')
async def rwanda_by_search(message: Message):
    command="Rwanda"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ruanda-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Руанду.", reply_markup=keyboard_menu)

# Румыния
@dp.message_handler(lambda message: message.text.lower() == 'румыния' or message.text.lower() == 'romania' or message.text.lower() == 'hevsybz')
async def romania_by_search(message: Message):
    command="Romania"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Rumyniya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Румынию.", reply_markup=keyboard_menu)

# Сальвадор
@dp.message_handler(lambda message: message.text.lower() == 'сальвадор' or message.text.lower() == 'salvador' or message.text.lower() == 'cfkmdfljh')
async def salvador_by_search(message: Message): 
    command="Salvador"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Salvador-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сальвадор.", reply_markup=keyboard_menu)

# Сан-Марино
@dp.message_handler(lambda message: message.text.lower() == 'сан-марино' or message.text.lower() == 'сан марино' or message.text.lower() == 'san marino' or message.text.lower() == 'cfy vfhbyj' or message.text.lower() == 'cfy-vfhbyj')
async def san_marino_by_search(message: Message): 
    command="San Marino"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/San-Marino-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сан-Марино.", reply_markup=keyboard_menu)

# Сан-Томе и Принсипи
@dp.message_handler(lambda message: message.text.lower() == 'сан-томе и принсипи' or message.text.lower() == 'сан-томе' or message.text.lower() == 'сан томе' or message.text.lower() == 'принсипи' or message.text.lower() == 'sao tome and principe' or message.text.lower() == 'principe' or message.text.lower() == 'sao tome' or message.text.lower() == 'cfy-njvt b ghbycbgb' or message.text.lower() == 'cfy-njvt' or message.text.lower() == 'cfy njvt' or message.text.lower() == 'ghbycbgb' or message.text.lower() == 'cfy njvt b ghbycbgb')
async def sao_tome_and_principe_by_search(message: Message): 
    command="Sao Tome and Principe"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/San-Tome-i-Prinsipi-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сан-Томе и Принсипи.", reply_markup=keyboard_menu)

# Саудовская Аравия
@dp.message_handler(lambda message: message.text.lower() == 'саудовская аравия' or message.text.lower() == 'saudi arabia' or message.text.lower() == 'cfeljdcrfz fhfdbz')
async def saudi_arabia_by_search(message: Message): 
    command="Saudi Arabia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Saudovskaya-Araviya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Саудовскую Аравию.", reply_markup=keyboard_menu)

# Северные Марианские острова
@dp.message_handler(lambda message: message.text.lower() == 'северные марианские острова' or message.text.lower() == 'марианские острова' or message.text.lower() == 'марианские' or message.text.lower() == 'northern mariana islands' or message.text.lower() == 'mariana islands' or message.text.lower() == 'mariana' or message.text.lower() == 'ctdthyst vfhbfycrbt jcnhjdf' or message.text.lower() == 'vfhbfycrbt jcnhjdf' or message.text.lower() == 'vfhbfycrbt')
async def northern_mariana_islands_by_search(message: Message): 
    command="Northern Mariana islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Severnye-Marianskie-ostrova-poehali-05-02')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Северные Марианские острова.", reply_markup=keyboard_menu)

# Сейшельские Острова (Сейшелы)
@dp.message_handler(lambda message: message.text.lower() == 'сейшельские острова' or message.text.lower() == 'сейшелы' or message.text.lower() == 'seychelles' or message.text.lower() == 'ctqitkmcrbt jcnhjdf' or message.text.lower() == 'ctqitks')
async def seychelles_by_search(message: Message): 
    command="Seychelles"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Sejshelskie-Ostrova-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Сейшельские Острова.", reply_markup=keyboard_menu)

# Сенегал
@dp.message_handler(lambda message: message.text.lower() == 'сенегал' or message.text.lower() == 'senegal' or message.text.lower() == 'ctytufk')
async def senegal_by_search(message: Message): 
    command="Senegal"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Senegal-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сенегал.", reply_markup=keyboard_menu)

"""
# Сен-Пьер и Микелон
@dp.message_handler(lambda message: message.text.lower() == 'сен-пьер и микелон' or message.text.lower() == 'сен-пьер' or message.text.lower() == 'сен пьер' or message.text.lower() == 'микелон' or message.text.lower() == 'miquelon' or message.text.lower() == 'saint-pierre and miquelon' or message.text.lower() == 'saint pierre' or message.text.lower() == 'saint-pierre' or message.text.lower() == 'vbrtkjy' or message.text.lower() == 'cty-gmth b vbrtkjy' or message.text.lower() == 'cty-gmth' or message.text.lower() == 'cty gmth')
async def saint_pierre_and_miquelon_by_search(message: Message): 
    command="Saint-Pierre and Miquelon"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Braziliya-Sen-Per-i-Mikelon-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сен-Пьер и Микелон.", reply_markup=keyboard_menu)
"""
    
# Сент-Винсент и Гренадины
@dp.message_handler(lambda message: message.text.lower() == 'сент-винсент и гренадины' or message.text.lower() == 'сент-винсент' or message.text.lower() == 'сент винсент' or message.text.lower() == 'гренадины' or message.text.lower() == 'st. vincent' or message.text.lower() == 'saint vincent and grenadines' or message.text.lower() == 'saint vincent' or message.text.lower() == 'grenadines' or message.text.lower() == 'ctyn-dbyctyn b uhtyflbys' or message.text.lower() == 'uhtyflbys' or message.text.lower() == 'ctyn dbyctyn' or message.text.lower() == 'ctyn-dbyctyn')
async def saint_vincent_and_grenadines_by_search(message: Message): 
    command="Saint Vincent and Grenadines"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Sent-Vinsent-i-Grenadiny-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сент-Винсент и Гренадины.", reply_markup=keyboard_menu)

# Сент-Китс и Невис
@dp.message_handler(lambda message: message.text.lower() == 'сент-китс и невис' or message.text.lower() == 'сент-китс' or message.text.lower() == 'сент китс' or message.text.lower() == 'невис' or message.text.lower() == 'saint kitts and nevis' or message.text.lower() == 'saint kitts' or message.text.lower() == 'nevis' or message.text.lower() == 'ctyn-rbnc b ytdbc' or message.text.lower() == 'ctyn-rbnc' or message.text.lower() == 'ctyn rbnc' or message.text.lower() == 'ytdbc')
async def saint_kitts_and_nevis_by_search(message: Message): 
    command="Saint Kitts and Nevis"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Sent-Kits-i-Nevis-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сент-Китс и Невис.", reply_markup=keyboard_menu)

# Сент-Люсия
@dp.message_handler(lambda message: message.text.lower() == 'сент-люсия' or message.text.lower() == 'сент люсия' or message.text.lower() == 'saint lucia' or message.text.lower() == 'ctyn k.cbz' or message.text.lower() == 'ctyn-k.cbz')
async def saint_lucia_by_search(message: Message): 
    command="Saint Lucia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Sent-Lyusiya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сент-Люсию.", reply_markup=keyboard_menu)

# Сербия
@dp.message_handler(lambda message: message.text.lower() == 'сербия' or message.text.lower() == 'serbia' or message.text.lower() == 'cth,bz')
async def serbia_by_search(message: Message): 
    command="Serbia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Serbiya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сербию.", reply_markup=keyboard_menu)

# Сингапур
@dp.message_handler(lambda message: message.text.lower() == 'сингапур' or message.text.lower() == 'singapore' or message.text.lower() == 'cbyufgeh')
async def singapore_by_search(message: Message): 
    command="Singapore"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Singapur-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сингапур.", reply_markup=keyboard_menu)

# Сирия
@dp.message_handler(lambda message: message.text.lower() == 'сирия' or message.text.lower() == 'syria' or message.text.lower() == 'cbhbz')
async def syria_by_search(message: Message): 
    command="Syria"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Siriya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сирию.", reply_markup=keyboard_menu)

# Словакия
@dp.message_handler(lambda message: message.text.lower() == 'словакия' or message.text.lower() == 'slovakia' or message.text.lower() == 'ckjdfrbz')
async def slovakia_by_search(message: Message): 
    command="Slovakia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Slovakiya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Словакию.", reply_markup=keyboard_menu)

# Словения
@dp.message_handler(lambda message: message.text.lower() == 'словения' or message.text.lower() == 'slovenia' or message.text.lower() == 'ckjdtybz')
async def slovenia_by_search(message: Message): 
    command="Slovenia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Sloveniya-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Словению.", reply_markup=keyboard_menu)

# Соломоновы острова
@dp.message_handler(lambda message: message.text.lower() == 'соломоновы острова' or message.text.lower() == 'соломоновы' or message.text.lower() == 'solomon islands' or message.text.lower() == 'solomon' or message.text.lower() == 'cjkjvjyjds jcnhjdf' or message.text.lower() == 'cjkjvjyjds')
async def solomon_islands_by_search(message: Message): 
    command="Solomon islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Solomonovy-ostrova-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Соломоновы острова.", reply_markup=keyboard_menu)

# Сомали
@dp.message_handler(lambda message: message.text.lower() == 'сомали' or message.text.lower() == 'somalia' or message.text.lower() == 'cjvfkb')
async def somalia_by_search(message: Message): 
    command="Somalia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Somali-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сомали.", reply_markup=keyboard_menu)

# Республика Судан
@dp.message_handler(lambda message: message.text.lower() == 'республика судан' or message.text.lower() == 'republic of sudan' or message.text.lower() == 'htcge,kbrf celfy')
async def republic_of_sudan_by_search(message: Message): 
    command="Republic of Sudan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Sudan-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Республику Судан.", reply_markup=keyboard_menu)

# Суринам
@dp.message_handler(lambda message: message.text.lower() == 'суринам' or message.text.lower() == 'suriname' or message.text.lower() == 'cehbyfv')
async def suriname_by_search(message: Message): 
    command="Suriname"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Surinam-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Суринам.", reply_markup=keyboard_menu)

# США (Америка)
@dp.message_handler(lambda message: message.text.lower() == 'сша' or message.text.lower() == 'америка' or message.text.lower() == 'соединенные штаты америки' or message.text.lower() == 'united states of america' or message.text.lower() == 'usa' or message.text.lower() == 'america' or message.text.lower() == 'fvthbrf' or message.text.lower() == 'cif' or message.text.lower() == 'cjtlbytyyst infns fvthbrb')
async def usa_by_search(message: Message): 
    command="USA"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/SSHA-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в США.", reply_markup=keyboard_menu)

# Сьерра-Леоне
@dp.message_handler(lambda message: message.text.lower() == 'сьерра-леоне' or message.text.lower() == 'сьерра леоне' or message.text.lower() == 'sierra leone' or message.text.lower() == 'cmthhf ktjyt' or message.text.lower() == 'cmthhf-ktjyt')
async def sierra_leone_by_search(message: Message): 
    command="Sierra Leone"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Serra-Leone-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Сьерра-Леоне.", reply_markup=keyboard_menu)

# Таджикистан
@dp.message_handler(lambda message: message.text.lower() == 'таджикистан' or message.text.lower() == 'tajikistan' or message.text.lower() == 'nfl;brbcnfy')
async def tajikistan_by_search(message: Message):
    command="Tajikistan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tadzhikistan-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Таджикистан.", reply_markup=keyboard_menu)

# Тайвань
@dp.message_handler(lambda message: message.text.lower() == 'тайвань' or message.text.lower() == 'taiwan' or message.text.lower() == 'nfqdfym')
async def taiwan_by_search(message: Message):
    command="Taiwan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tajvan-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Тайвань.", reply_markup=keyboard_menu)

# Таиланд (Тайланд)
@dp.message_handler(lambda message: message.text.lower() == 'таиланд' or message.text.lower() == 'тайланд' or message.text.lower() == 'thailand' or message.text.lower() == 'nfqkfyl' or message.text.lower() == 'nfbkfyl')
async def thailand_by_search(message: Message):
    command="Thailand"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tailand-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Таиланд.", reply_markup=keyboard_menu)

# Танзания
@dp.message_handler(lambda message: message.text.lower() == 'танзания' or message.text.lower() == 'tanzania' or message.text.lower() == 'nfypfybz')
async def tanzania_by_search(message: Message):
    command="Tanzania"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tanzaniya-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Танзанию.", reply_markup=keyboard_menu)

# Теркс и Кайкос
@dp.message_handler(lambda message: message.text.lower() == 'теркс и кайкос' or message.text.lower() == 'turks and caicos' or message.text.lower() == 'nthrc b rfqrjc')
async def turks_and_caicos_by_search(message: Message):
    command="Turks and Caicos"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Terks-i-Kajkos-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Теркс и Кайкос.", reply_markup=keyboard_menu)

# Того
@dp.message_handler(lambda message: message.text.lower() == 'того' or message.text.lower() == 'togo' or message.text.lower() == 'njuj')
async def togo_by_search(message: Message):
    command="Togo"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Togo-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Того.", reply_markup=keyboard_menu)

"""
# Токелау
@dp.message_handler(lambda message: message.text.lower() == 'токелау' or message.text.lower() == 'tokelau' or message.text.lower() == 'njrtkfe')
async def tokelau_by_search(message: Message):
    command="Tokelau"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tokelau-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Токелау.", reply_markup=keyboard_menu)
"""

# Тонга
@dp.message_handler(lambda message: message.text.lower() == 'тонга' or message.text.lower() == 'tonga' or message.text.lower() == 'njyuf')
async def tonga_by_search(message: Message):
    command="Tonga"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tonga-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Тонгу.", reply_markup=keyboard_menu)

# Тринидад и Тобаго
@dp.message_handler(lambda message: message.text.lower() == 'тринидад и тобаго' or message.text.lower() == 'тринидад' or message.text.lower() == 'тобаго' or message.text.lower() == 'trinidad and tobago' or message.text.lower() == 'trinidad' or message.text.lower() == 'tobago' or message.text.lower() == 'nhbyblfl' or message.text.lower() == 'nj,fuj' or message.text.lower() == 'nhbyblfl b nj,fuj')
async def trinidad_and_tobago_by_search(message: Message):
    command="Trinidad and Tobago"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Trinidad-i-Tobago-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Тринидад и Тобаго.", reply_markup=keyboard_menu)

# Тувалу
@dp.message_handler(lambda message: message.text.lower() == 'тувалу' or message.text.lower() == 'tuvalu' or message.text.lower() == 'nedfke')
async def tuvalu_by_search(message: Message):
    command="Tuvalu"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tuvalu-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Тувалу.", reply_markup=keyboard_menu)

# Тунис
@dp.message_handler(lambda message: message.text.lower() == 'тунис' or message.text.lower() == 'tunisia' or message.text.lower() == 'neybc')
async def tunisia_by_search(message: Message):
    command="Tunisia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Tunis-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Тунис.", reply_markup=keyboard_menu)

# Туркменистан
@dp.message_handler(lambda message: message.text.lower() == 'туркменистан' or message.text.lower() == 'turkmenistan' or message.text.lower() == 'nehrvtybcnfy')
async def turkmenistan_by_search(message: Message):
    command="Turkmenistan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Turkmenistan-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Туркменистан.", reply_markup=keyboard_menu)

# Турция
@dp.message_handler(lambda message: message.text.lower() == 'турция' or message.text.lower() == 'turkey' or message.text.lower() == 'nehwbz')
async def turkey_by_search(message: Message): 
    command="Turkey"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Turciya-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Турцию.", reply_markup=keyboard_menu)

# Уганда
@dp.message_handler(lambda message: message.text.lower() == 'уганда' or message.text.lower() == 'uganda' or message.text.lower() == 'eufylf')
async def uganda_by_search(message: Message): 
    command="Uganda"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Uganda-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Уганду.", reply_markup=keyboard_menu)

# Узбекистан
@dp.message_handler(lambda message: message.text.lower() == 'узбекистан' or message.text.lower() == 'uzbekistan' or message.text.lower() == 'ep,trbcnfy')
async def uzbekistan_by_search(message: Message): 
    command="Uzbekistan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Uzbekistan-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Узбекистан.", reply_markup=keyboard_menu)

# Украина
@dp.message_handler(lambda message: message.text.lower() == 'украина' or message.text.lower() == 'ukraine' or message.text.lower() == 'erhfbyf')
async def ukraine_by_search(message: Message): 
    command="Ukraine"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Ukraina-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Украину.", reply_markup=keyboard_menu)

# Уругвай
@dp.message_handler(lambda message: message.text.lower() == 'уругвай' or message.text.lower() == 'uruguay' or message.text.lower() == 'eheudfq')
async def uruguay_by_search(message: Message): 
    command="Uruguay"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Urugvaj-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Уругвай.", reply_markup=keyboard_menu)

"""
# ??? Фарерские острова
@dp.message_handler(lambda message: message.text.lower() == 'фарерские острова' or message.text.lower() == 'faroe islands' or message.text.lower() == 'afhthcrbt jcnhjdf')
async def faroe_islands_by_search(message: Message): 
    command="Faroe Islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Farerskie-ostrova-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Фарерские острова.", reply_markup=keyboard_menu)
"""

# Фиджи
@dp.message_handler(lambda message: message.text.lower() == 'фиджи' or message.text.lower() == 'fiji' or message.text.lower() == 'abl;b')
async def fiji_by_search(message: Message): 
    command="Fiji"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Fidzhi-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Фиджи.", reply_markup=keyboard_menu)

# Филиппины
@dp.message_handler(lambda message: message.text.lower() == 'филиппины' or message.text.lower() == 'philippines' or message.text.lower() == 'abkbggbys')
async def philippines_by_search(message: Message): 
    command="Philippines"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Filippiny-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Филиппины.", reply_markup=keyboard_menu)

# Финляндия
@dp.message_handler(lambda message: message.text.lower() == 'финляндия' or message.text.lower() == 'finland' or message.text.lower() == 'abykzylbz')
async def finland_by_search(message: Message): 
    command="Finland"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Finlyandiya-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Финляндию.", reply_markup=keyboard_menu)

# Фолклендские острова
@dp.message_handler(lambda message: message.text.lower() == 'фолклендские острова' or message.text.lower() == 'фолклендские' or message.text.lower() == 'falkland islands' or message.text.lower() == 'falkland' or message.text.lower() == 'ajkrktylcrbt' or message.text.lower() == 'ajkrktylcrbt jcnhjdf')
async def falkland_islands_by_search(message: Message): 
    command="Falkland Islands"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Folklendskie-ostrova-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Фолклендские острова.", reply_markup=keyboard_menu)

# Франция 
@dp.message_handler(lambda message: message.text.lower() == 'франция' or message.text.lower() == 'france' or message.text.lower() == 'ahfywbz')
async def france_by_search(message: Message): 
    command="France"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Franciya-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда во Францию.", reply_markup=keyboard_menu)

"""
# ??? Французская Гваделупа (Гваделупа)
@dp.message_handler(lambda message: message.text.lower() == 'французская гваделупа' or message.text.lower() == 'гваделупа' or message.text.lower() == 'guadeloupe' or message.text.lower() == 'french guadeloupe' or message.text.lower() == 'udfltkegf' or message.text.lower() == 'ahfywepcrfz udfltkegf')
async def guadeloupe_by_search(message: Message): 
    command="Guadeloupe"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Francuzskaya-Gvadelupa-Gvadelupa-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гваделупу.", reply_markup=keyboard_menu)
"""

# ? Французская Гвиана (Гвиана)
@dp.message_handler(lambda message: message.text.lower() == 'французская гвиана' or message.text.lower() == 'гвиана' or message.text.lower() == 'french guiana' or message.text.lower() == 'guiana' or message.text.lower() == 'udbfyf' or message.text.lower() == 'ahfywepcrfz udbfyf')
async def guiana_by_search(message: Message): 
    command="Guiana"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Francuzskaya-Gviana-Gviana-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Гвиану.", reply_markup=keyboard_menu)

# ? Французская Полинезия (Полинезия)
@dp.message_handler(lambda message: message.text.lower() == 'французская полинезия' or message.text.lower() == 'полинезия' or message.text.lower() == 'polynesia' or message.text.lower() == 'french polynesia' or message.text.lower() == 'gjkbytpbz' or message.text.lower() == 'ahfywepcrfz gjkbytpbz')
async def french_polynesia_by_search(message: Message): 
    command="French polynesia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Francuzskaya-Polineziya-Polineziya-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда во Французскую Полинезию.", reply_markup=keyboard_menu)

# Хорватия
@dp.message_handler(lambda message: message.text.lower() == 'хорватия' or message.text.lower() == 'croatia' or message.text.lower() == '[jhdfnbz]')
async def croatia_by_search(message: Message): 
    command="Croatia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Horvatiya-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Хорватию.", reply_markup=keyboard_menu)

# Центральноафриканская Республика (ЦАР)
@dp.message_handler(lambda message: message.text.lower() == 'центральноафриканская республика' or message.text.lower() == 'цар' or message.text.lower() == 'central african republic' or message.text.lower() == 'car' or message.text.lower() == 'wtynhfkmyjfahbrfycrfz htcge,kbrf' or message.text.lower() == 'wfh')
async def car_by_search(message: Message): 
    command="CAR"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/Centralnoafrikanskaya-Respublika-poehali-05-04')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Центральноафриканскую Республику.", reply_markup=keyboard_menu)

# Чад
@dp.message_handler(lambda message: message.text.lower() == 'чад' or message.text.lower() == 'chad' or message.text.lower() == 'xfl')
async def chad_by_search(message: Message): 
    command="Chad"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/CHad-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Чад.", reply_markup=keyboard_menu)

# Черногория
@dp.message_handler(lambda message: message.text.lower() == 'черногория' or message.text.lower() == 'montenegro' or message.text.lower() == 'xthyjujhbz')
async def montenegro_by_search(message: Message): 
    command="Montenegro"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/CHernogoriya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Черногорию.", reply_markup=keyboard_menu)

# Чехия
@dp.message_handler(lambda message: message.text.lower() == 'чехия' or message.text.lower() == 'czech' or message.text.lower() == 'czech republic' or message.text.lower() == 'xt[bz')
async def czech_by_search(message: Message): 
    command="Czech"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/CHehiya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Чехию.", reply_markup=keyboard_menu)

# Чили
@dp.message_handler(lambda message: message.text.lower() == 'чили' or message.text.lower() == 'chile' or message.text.lower() == 'xbkb')
async def chile_by_search(message: Message): 
    command="Chile"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/CHili-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Чили.", reply_markup=keyboard_menu)

# Швейцария
@dp.message_handler(lambda message: message.text.lower() == 'швейцария' or message.text.lower() == 'switzerland' or message.text.lower() == 'idtqwfhbz')
async def switzerland_by_search(message: Message): 
    command="Switzerland"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/SHvejcariya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Швейцарию.", reply_markup=keyboard_menu)

# Швеция
@dp.message_handler(lambda message: message.text.lower() == 'швеция' or message.text.lower() == 'sweden' or message.text.lower() == 'idtwbz')
async def sweden_by_search(message: Message): 
    command="Sweden"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/SHveciya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Швецию.", reply_markup=keyboard_menu)

"""
# ??? Шпицберген
@dp.message_handler(lambda message: message.text.lower() == 'шпицберген' or message.text.lower() == 'svalbard' or message.text.lower() == 'spitsbergen' or message.text.lower() == 'igbw,thuty')
async def spitsbergen_by_search(message: Message): 
    command="Spitsbergen"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/SHpicbergen-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Шпицберген.", reply_markup=keyboard_menu)
"""

# Шри-Ланка
@dp.message_handler(lambda message: message.text.lower() == 'шри-ланка' or message.text.lower() == 'шри ланка' or message.text.lower() == 'sri lanka' or message.text.lower() == 'ihb-kfyrf' or message.text.lower() == 'ihb kfyrf')
async def sri_lanka_by_search(message: Message): 
    command="Sri Lanka"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/SHri-Lanka-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда на Шри-Ланку.", reply_markup=keyboard_menu)

# Эквадор
@dp.message_handler(lambda message: message.text.lower() == 'эквадор' or message.text.lower() == 'ecuador' or message.text.lower() == '\'rdfljh')
async def ecuador_by_search(message: Message): 
    command="Ecuador"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/EHkvador-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Эквадор.", reply_markup=keyboard_menu)

# Экваториальная Гвинея
@dp.message_handler(lambda message: message.text.lower() == 'экваториальная гвинея' or message.text.lower() == 'equatorial guinea' or message.text.lower() == '\'rdfnjhbfkmyfz udbytz')
async def equatorial_guinea_by_search(message: Message): 
    command="Equatorial Guinea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/EHkvatorialnaya-Gvineya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Экваториальную Гвинею.", reply_markup=keyboard_menu)

# Эритрея
@dp.message_handler(lambda message: message.text.lower() == 'эритрея' or message.text.lower() == 'erythrea' or message.text.lower() == '\'hbnhtz')
async def erythrea_by_search(message: Message): 
    command="Erythrea"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/EHritreya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Эритрею.", reply_markup=keyboard_menu)

# Эсватини
@dp.message_handler(lambda message: message.text.lower() == 'эсватини' or message.text.lower() == 'eswatini' or message.text.lower() == '\'cdfnbyb')
async def eswatini_by_search(message: Message): 
    command="Eswatini"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/EHsvatini-poehali-05-03')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Эсватини.", reply_markup=keyboard_menu)

# Эстония
@dp.message_handler(lambda message: message.text.lower() == 'эстония' or message.text.lower() == 'estonia' or message.text.lower() == '\'cnjybz')
async def estonia_by_search(message: Message): 
    command="Estonia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/EHstoniya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Эстонию.", reply_markup=keyboard_menu)

# Эфиопия
@dp.message_handler(lambda message: message.text.lower() == 'эфиопия' or message.text.lower() == 'ethiopia' or message.text.lower() == '\'abjgbz')
async def ethiopia_by_search(message: Message): 
    command="Ethiopia"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/EHfiopiya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Эфиопию.", reply_markup=keyboard_menu)

# ЮАР
@dp.message_handler(lambda message: message.text.lower() == 'юар' or message.text.lower() == 'south africa' or message.text.lower() == '.fh')
async def south_africa_by_search(message: Message): 
    command="South Africa"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/YUzhno-Afrikanskaya-Respublika-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в ЮАР.", reply_markup=keyboard_menu)

# Южный Судан
@dp.message_handler(lambda message: message.text.lower() == 'южный судан' or message.text.lower() == 'south sudan' or message.text.lower() == '.;ysq celfy')
async def south_sudan_by_search(message: Message): 
    command="South Sudan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/YUzhnyj-Sudan-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Южный Судан.", reply_markup=keyboard_menu)

# Ямайка
@dp.message_handler(lambda message: message.text.lower() == 'ямайка' or message.text.lower() == 'jamaica' or message.text.lower() == 'zvfqrf')
async def jamaica_by_search(message: Message): 
    command="Jamaica"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/YAmajka-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Ямайку.", reply_markup=keyboard_menu)

# Япония
@dp.message_handler(lambda message: message.text.lower() == 'япония' or message.text.lower() == 'japan' or message.text.lower() == 'zgjybz')
async def japan_by_search(message: Message): 
    command="Japan"
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    data_month = datetime.datetime.today().strftime("%m")
    data_day = datetime.datetime.today().strftime("%d")
    data_year = datetime.datetime.today().strftime("%Y")
    with open('history.csv', 'a', newline="", encoding='UTF-8') as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow([user_id, user_full_name, data_month, data_day, data_year, command])

    logging.info(f'{user_id} {user_full_name} {time.asctime()} {command}')
    await message.answer(f"{hide_link('https://telegra.ph/YAponiya-poehali-05-05')}" f"В этой статье вы найдете всю актуальную информацию о правилах въезда в Японию.", reply_markup=keyboard_menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = False)