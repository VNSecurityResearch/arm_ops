
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xba\xb3^\xd3>\xb8z\xe9\xaaL\xac\xc5\x07\xbdN\xa8'
    
_lr_action_items = {'B':([0,],[2,]),'IP':([2,],[5,]),'SP':([2,],[9,]),'PC':([2,],[7,]),'LR':([2,],[8,]),'REGISTER':([2,],[4,]),'$end':([1,3,4,5,6,7,8,9,10,],[0,-1,-6,-7,-13,-10,-9,-8,-14,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,],[1,]),'register':([2,],[6,]),'command':([0,],[3,]),'branchtarget':([2,],[10,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> command','line',1,'p_line','parser.py',5),
  ('argument -> HEXNUM','argument',1,'p_argument_h','parser.py',13),
  ('argument -> CONSTNUM','argument',1,'p_argument_i','parser.py',18),
  ('argument -> register','argument',1,'p_argument_r','parser.py',22),
  ('argument -> CHAR','argument',1,'p_argument_c','parser.py',26),
  ('register -> REGISTER','register',1,'p_register','parser.py',34),
  ('register -> IP','register',1,'p_register_fp','parser.py',41),
  ('register -> SP','register',1,'p_register_sp','parser.py',45),
  ('register -> LR','register',1,'p_register_lr','parser.py',49),
  ('register -> PC','register',1,'p_register_pc','parser.py',53),
  ('target -> IMMTARGET','target',1,'p_target_imm','parser.py',61),
  ('target -> IMMHEXTARGET','target',1,'p_target_immhex','parser.py',65),
  ('branchtarget -> register','branchtarget',1,'p_branchtarget_addr','parser.py',73),
  ('command -> B branchtarget','command',2,'p_brch','parser.py',88),
]
