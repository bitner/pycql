
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'condition_or_emptyleftEQNEleftGTGELTLEleftPLUSMINUSleftTIMESDIVIDEAFTER AND ATTRIBUTE BBOX BEFORE BETWEEN BEYOND COMMA CONTAINS CROSSES DISJOINT DIVIDE DURATION DURING DWITHIN ENVELOPE EQ EQUALS FLOAT GE GEOMETRY GT ILIKE IN INTEGER INTERSECTS IS LBRACKET LE LIKE LPAREN LT MINUS NE NOT NULL OR OVERLAPS PLUS QUOTED RBRACKET RELATE RPAREN TIME TIMES TOUCHES UNITS WITHIN feet kilometers meters nautical miles statute miles condition_or_empty : condition\n                               | empty\n         condition : predicate\n                      | condition AND condition\n                      | condition OR condition\n                      | NOT condition\n                      | LPAREN condition RPAREN\n                      | LBRACKET condition RBRACKET\n         predicate : expression EQ expression\n                      | expression NE expression\n                      | expression LT expression\n                      | expression LE expression\n                      | expression GT expression\n                      | expression GE expression\n                      | expression NOT BETWEEN expression AND expression\n                      | expression BETWEEN expression AND expression\n                      | expression NOT LIKE QUOTED\n                      | expression LIKE QUOTED\n                      | expression NOT ILIKE QUOTED\n                      | expression ILIKE QUOTED\n                      | expression NOT IN LPAREN expression_list RPAREN\n                      | expression IN LPAREN expression_list RPAREN\n                      | expression IS NOT NULL\n                      | expression IS NULL\n                      | temporal_predicate\n                      | spatial_predicate\n         temporal_predicate : expression BEFORE TIME\n                               | expression BEFORE OR DURING time_period\n                               | expression DURING time_period\n                               | expression DURING OR AFTER time_period\n                               | expression AFTER TIME\n         time_period : TIME DIVIDE TIME\n                        | TIME DIVIDE DURATION\n                        | DURATION DIVIDE TIME\n         spatial_predicate : INTERSECTS LPAREN expression COMMA expression RPAREN\n                              | DISJOINT LPAREN expression COMMA expression RPAREN\n                              | CONTAINS LPAREN expression COMMA expression RPAREN\n                              | WITHIN LPAREN expression COMMA expression RPAREN\n                              | TOUCHES LPAREN expression COMMA expression RPAREN\n                              | CROSSES LPAREN expression COMMA expression RPAREN\n                              | OVERLAPS LPAREN expression COMMA expression RPAREN\n                              | EQUALS LPAREN expression COMMA expression RPAREN\n                              | RELATE LPAREN expression COMMA expression COMMA QUOTED RPAREN\n                              | DWITHIN LPAREN expression COMMA expression COMMA number COMMA UNITS RPAREN\n                              | BEYOND LPAREN expression COMMA expression COMMA number COMMA UNITS RPAREN\n                              | BBOX LPAREN expression COMMA number COMMA number COMMA number COMMA number RPAREN\n                              | BBOX LPAREN expression COMMA number COMMA number COMMA number COMMA number COMMA QUOTED RPAREN\n         expression_list : expression_list COMMA expression\n                            | expression\n         expression : expression PLUS expression\n                       | expression MINUS expression\n                       | expression TIMES expression\n                       | expression DIVIDE expression\n                       | LPAREN expression RPAREN\n                       | LBRACKET expression RBRACKET\n                       | GEOMETRY\n                       | ENVELOPE\n                       | attribute\n                       | QUOTED\n                       | INTEGER\n                       | FLOAT\n         number : INTEGER\n                   | FLOAT\n         attribute : ATTRIBUTE\n        empty : '
    
_lr_action_items = {'NOT':([0,5,6,7,8,9,12,13,14,15,16,29,30,31,34,36,48,71,73,92,93,94,95,],[5,5,5,5,43,-59,-56,-57,-58,-60,-61,-64,5,5,43,43,90,-54,-55,-50,-51,-52,-53,]),'LPAREN':([0,5,6,7,17,18,19,20,21,22,23,24,25,26,27,28,30,31,37,38,39,40,41,42,44,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,85,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[6,6,6,6,56,57,58,59,60,61,62,63,64,65,66,67,6,6,75,75,75,75,75,75,75,89,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,120,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'LBRACKET':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[7,7,7,7,7,7,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'$end':([0,1,2,3,4,9,10,11,12,13,14,15,16,29,32,68,69,70,71,72,73,74,77,78,79,80,81,87,88,91,92,93,94,95,96,98,102,118,119,124,143,144,146,147,148,149,150,165,166,168,169,170,171,172,173,174,175,184,191,192,196,198,],[-65,0,-1,-2,-3,-59,-25,-26,-56,-57,-58,-60,-61,-64,-6,-4,-5,-7,-54,-8,-55,-9,-10,-11,-12,-13,-14,-18,-20,-24,-50,-51,-52,-53,-27,-29,-31,-17,-19,-23,-16,-22,-28,-30,-32,-33,-34,-15,-21,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,]),'GEOMETRY':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'ENVELOPE':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'QUOTED':([0,5,6,7,30,31,37,38,39,40,41,42,44,45,46,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,83,84,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,176,195,],[9,9,9,9,9,9,9,9,9,9,9,9,9,87,88,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,118,119,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,180,197,]),'INTEGER':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,140,141,145,177,178,179,187,193,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,163,15,15,163,163,163,163,163,]),'FLOAT':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,140,141,145,177,178,179,187,193,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,164,16,16,164,164,164,164,164,]),'INTERSECTS':([0,5,6,7,30,31,],[17,17,17,17,17,17,]),'DISJOINT':([0,5,6,7,30,31,],[18,18,18,18,18,18,]),'CONTAINS':([0,5,6,7,30,31,],[19,19,19,19,19,19,]),'WITHIN':([0,5,6,7,30,31,],[20,20,20,20,20,20,]),'TOUCHES':([0,5,6,7,30,31,],[21,21,21,21,21,21,]),'CROSSES':([0,5,6,7,30,31,],[22,22,22,22,22,22,]),'OVERLAPS':([0,5,6,7,30,31,],[23,23,23,23,23,23,]),'EQUALS':([0,5,6,7,30,31,],[24,24,24,24,24,24,]),'RELATE':([0,5,6,7,30,31,],[25,25,25,25,25,25,]),'DWITHIN':([0,5,6,7,30,31,],[26,26,26,26,26,26,]),'BEYOND':([0,5,6,7,30,31,],[27,27,27,27,27,27,]),'BBOX':([0,5,6,7,30,31,],[28,28,28,28,28,28,]),'ATTRIBUTE':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'AND':([2,4,9,10,11,12,13,14,15,16,29,32,33,35,68,69,70,71,72,73,74,77,78,79,80,81,86,87,88,91,92,93,94,95,96,98,102,117,118,119,124,143,144,146,147,148,149,150,165,166,168,169,170,171,172,173,174,175,184,191,192,196,198,],[30,-3,-59,-25,-26,-56,-57,-58,-60,-61,-64,30,30,30,30,30,-7,-54,-8,-55,-9,-10,-11,-12,-13,-14,121,-18,-20,-24,-50,-51,-52,-53,-27,-29,-31,141,-17,-19,-23,-16,-22,-28,-30,-32,-33,-34,-15,-21,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,]),'OR':([2,4,9,10,11,12,13,14,15,16,29,32,33,35,53,54,68,69,70,71,72,73,74,77,78,79,80,81,87,88,91,92,93,94,95,96,98,102,118,119,124,143,144,146,147,148,149,150,165,166,168,169,170,171,172,173,174,175,184,191,192,196,198,],[31,-3,-59,-25,-26,-56,-57,-58,-60,-61,-64,31,31,31,97,99,31,31,-7,-54,-8,-55,-9,-10,-11,-12,-13,-14,-18,-20,-24,-50,-51,-52,-53,-27,-29,-31,-17,-19,-23,-16,-22,-28,-30,-32,-33,-34,-15,-21,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,]),'RPAREN':([4,9,10,11,12,13,14,15,16,29,32,33,34,68,69,70,71,72,73,74,77,78,79,80,81,87,88,91,92,93,94,95,96,98,102,115,118,119,122,123,124,142,143,144,146,147,148,149,150,151,152,153,154,155,156,157,158,163,164,165,166,167,168,169,170,171,172,173,174,175,180,184,188,189,191,192,194,196,197,198,],[-3,-59,-25,-26,-56,-57,-58,-60,-61,-64,-6,70,71,-4,-5,-7,-54,-8,-55,-9,-10,-11,-12,-13,-14,-18,-20,-24,-50,-51,-52,-53,-27,-29,-31,71,-17,-19,-49,144,-23,166,-16,-22,-28,-30,-32,-33,-34,168,169,170,171,172,173,174,175,-62,-63,-15,-21,-48,-35,-36,-37,-38,-39,-40,-41,-42,184,-43,191,192,-44,-45,196,-46,198,-47,]),'RBRACKET':([4,9,10,11,12,13,14,15,16,29,32,35,36,68,69,70,71,72,73,74,77,78,79,80,81,87,88,91,92,93,94,95,96,98,102,116,118,119,124,143,144,146,147,148,149,150,165,166,168,169,170,171,172,173,174,175,184,191,192,196,198,],[-3,-59,-25,-26,-56,-57,-58,-60,-61,-64,-6,72,73,-4,-5,-7,-54,-8,-55,-9,-10,-11,-12,-13,-14,-18,-20,-24,-50,-51,-52,-53,-27,-29,-31,73,-17,-19,-23,-16,-22,-28,-30,-32,-33,-34,-15,-21,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,]),'EQ':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[37,-59,-56,-57,-58,-60,-61,-64,37,37,-54,-55,-50,-51,-52,-53,]),'NE':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[38,-59,-56,-57,-58,-60,-61,-64,38,38,-54,-55,-50,-51,-52,-53,]),'LT':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[39,-59,-56,-57,-58,-60,-61,-64,39,39,-54,-55,-50,-51,-52,-53,]),'LE':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[40,-59,-56,-57,-58,-60,-61,-64,40,40,-54,-55,-50,-51,-52,-53,]),'GT':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[41,-59,-56,-57,-58,-60,-61,-64,41,41,-54,-55,-50,-51,-52,-53,]),'GE':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[42,-59,-56,-57,-58,-60,-61,-64,42,42,-54,-55,-50,-51,-52,-53,]),'BETWEEN':([8,9,12,13,14,15,16,29,34,36,43,71,73,92,93,94,95,],[44,-59,-56,-57,-58,-60,-61,-64,44,44,82,-54,-55,-50,-51,-52,-53,]),'LIKE':([8,9,12,13,14,15,16,29,34,36,43,71,73,92,93,94,95,],[45,-59,-56,-57,-58,-60,-61,-64,45,45,83,-54,-55,-50,-51,-52,-53,]),'ILIKE':([8,9,12,13,14,15,16,29,34,36,43,71,73,92,93,94,95,],[46,-59,-56,-57,-58,-60,-61,-64,46,46,84,-54,-55,-50,-51,-52,-53,]),'IN':([8,9,12,13,14,15,16,29,34,36,43,71,73,92,93,94,95,],[47,-59,-56,-57,-58,-60,-61,-64,47,47,85,-54,-55,-50,-51,-52,-53,]),'IS':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[48,-59,-56,-57,-58,-60,-61,-64,48,48,-54,-55,-50,-51,-52,-53,]),'PLUS':([8,9,12,13,14,15,16,29,34,36,71,73,74,77,78,79,80,81,86,92,93,94,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,122,143,151,152,153,154,155,156,157,158,159,160,161,165,167,],[49,-59,-56,-57,-58,-60,-61,-64,49,49,-54,-55,49,49,49,49,49,49,49,-50,-51,-52,-53,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'MINUS':([8,9,12,13,14,15,16,29,34,36,71,73,74,77,78,79,80,81,86,92,93,94,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,122,143,151,152,153,154,155,156,157,158,159,160,161,165,167,],[50,-59,-56,-57,-58,-60,-61,-64,50,50,-54,-55,50,50,50,50,50,50,50,-50,-51,-52,-53,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'TIMES':([8,9,12,13,14,15,16,29,34,36,71,73,74,77,78,79,80,81,86,92,93,94,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,122,143,151,152,153,154,155,156,157,158,159,160,161,165,167,],[51,-59,-56,-57,-58,-60,-61,-64,51,51,-54,-55,51,51,51,51,51,51,51,51,51,-52,-53,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'DIVIDE':([8,9,12,13,14,15,16,29,34,36,71,73,74,77,78,79,80,81,86,92,93,94,95,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,122,143,151,152,153,154,155,156,157,158,159,160,161,165,167,],[52,-59,-56,-57,-58,-60,-61,-64,52,52,-54,-55,52,52,52,52,52,52,52,52,52,-52,-53,127,128,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'BEFORE':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,],[53,-59,-56,-57,-58,-60,-61,-64,53,53,-54,-55,-50,-51,-52,-53,]),'DURING':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,97,],[54,-59,-56,-57,-58,-60,-61,-64,54,54,-54,-55,-50,-51,-52,-53,125,]),'AFTER':([8,9,12,13,14,15,16,29,34,36,71,73,92,93,94,95,99,],[55,-59,-56,-57,-58,-60,-61,-64,55,55,-54,-55,-50,-51,-52,-53,126,]),'COMMA':([9,12,13,14,15,16,29,71,73,92,93,94,95,103,104,105,106,107,108,109,110,111,112,113,114,122,123,142,159,160,161,162,163,164,167,181,182,183,190,194,],[-59,-56,-57,-58,-60,-61,-64,-54,-55,-50,-51,-52,-53,129,130,131,132,133,134,135,136,137,138,139,140,-49,145,145,176,177,178,179,-62,-63,-48,185,186,187,193,195,]),'NULL':([48,90,],[91,124,]),'TIME':([53,54,55,125,126,127,128,],[96,100,102,100,100,148,150,]),'DURATION':([54,125,126,127,],[101,101,101,149,]),'UNITS':([185,186,],[188,189,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'condition_or_empty':([0,],[1,]),'condition':([0,5,6,7,30,31,],[2,32,33,35,68,69,]),'empty':([0,],[3,]),'predicate':([0,5,6,7,30,31,],[4,4,4,4,4,4,]),'expression':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[8,8,34,36,8,8,74,77,78,79,80,81,86,92,93,94,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,122,122,143,151,152,153,154,155,156,157,158,159,160,161,165,167,]),'temporal_predicate':([0,5,6,7,30,31,],[10,10,10,10,10,10,]),'spatial_predicate':([0,5,6,7,30,31,],[11,11,11,11,11,11,]),'attribute':([0,5,6,7,30,31,37,38,39,40,41,42,44,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,75,76,82,89,120,121,129,130,131,132,133,134,135,136,137,138,139,141,145,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'time_period':([54,125,126,],[98,146,147,]),'expression_list':([89,120,],[123,142,]),'number':([140,177,178,179,187,193,],[162,181,182,183,190,194,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> condition_or_empty","S'",1,None,None,None),
  ('condition_or_empty -> condition','condition_or_empty',1,'p_condition_or_empty','parser.py',86),
  ('condition_or_empty -> empty','condition_or_empty',1,'p_condition_or_empty','parser.py',87),
  ('condition -> predicate','condition',1,'p_condition','parser.py',92),
  ('condition -> condition AND condition','condition',3,'p_condition','parser.py',93),
  ('condition -> condition OR condition','condition',3,'p_condition','parser.py',94),
  ('condition -> NOT condition','condition',2,'p_condition','parser.py',95),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition','parser.py',96),
  ('condition -> LBRACKET condition RBRACKET','condition',3,'p_condition','parser.py',97),
  ('predicate -> expression EQ expression','predicate',3,'p_predicate','parser.py',110),
  ('predicate -> expression NE expression','predicate',3,'p_predicate','parser.py',111),
  ('predicate -> expression LT expression','predicate',3,'p_predicate','parser.py',112),
  ('predicate -> expression LE expression','predicate',3,'p_predicate','parser.py',113),
  ('predicate -> expression GT expression','predicate',3,'p_predicate','parser.py',114),
  ('predicate -> expression GE expression','predicate',3,'p_predicate','parser.py',115),
  ('predicate -> expression NOT BETWEEN expression AND expression','predicate',6,'p_predicate','parser.py',116),
  ('predicate -> expression BETWEEN expression AND expression','predicate',5,'p_predicate','parser.py',117),
  ('predicate -> expression NOT LIKE QUOTED','predicate',4,'p_predicate','parser.py',118),
  ('predicate -> expression LIKE QUOTED','predicate',3,'p_predicate','parser.py',119),
  ('predicate -> expression NOT ILIKE QUOTED','predicate',4,'p_predicate','parser.py',120),
  ('predicate -> expression ILIKE QUOTED','predicate',3,'p_predicate','parser.py',121),
  ('predicate -> expression NOT IN LPAREN expression_list RPAREN','predicate',6,'p_predicate','parser.py',122),
  ('predicate -> expression IN LPAREN expression_list RPAREN','predicate',5,'p_predicate','parser.py',123),
  ('predicate -> expression IS NOT NULL','predicate',4,'p_predicate','parser.py',124),
  ('predicate -> expression IS NULL','predicate',3,'p_predicate','parser.py',125),
  ('predicate -> temporal_predicate','predicate',1,'p_predicate','parser.py',126),
  ('predicate -> spatial_predicate','predicate',1,'p_predicate','parser.py',127),
  ('temporal_predicate -> expression BEFORE TIME','temporal_predicate',3,'p_temporal_predicate','parser.py',157),
  ('temporal_predicate -> expression BEFORE OR DURING time_period','temporal_predicate',5,'p_temporal_predicate','parser.py',158),
  ('temporal_predicate -> expression DURING time_period','temporal_predicate',3,'p_temporal_predicate','parser.py',159),
  ('temporal_predicate -> expression DURING OR AFTER time_period','temporal_predicate',5,'p_temporal_predicate','parser.py',160),
  ('temporal_predicate -> expression AFTER TIME','temporal_predicate',3,'p_temporal_predicate','parser.py',161),
  ('time_period -> TIME DIVIDE TIME','time_period',3,'p_time_period','parser.py',172),
  ('time_period -> TIME DIVIDE DURATION','time_period',3,'p_time_period','parser.py',173),
  ('time_period -> DURATION DIVIDE TIME','time_period',3,'p_time_period','parser.py',174),
  ('spatial_predicate -> INTERSECTS LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',179),
  ('spatial_predicate -> DISJOINT LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',180),
  ('spatial_predicate -> CONTAINS LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',181),
  ('spatial_predicate -> WITHIN LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',182),
  ('spatial_predicate -> TOUCHES LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',183),
  ('spatial_predicate -> CROSSES LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',184),
  ('spatial_predicate -> OVERLAPS LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',185),
  ('spatial_predicate -> EQUALS LPAREN expression COMMA expression RPAREN','spatial_predicate',6,'p_spatial_predicate','parser.py',186),
  ('spatial_predicate -> RELATE LPAREN expression COMMA expression COMMA QUOTED RPAREN','spatial_predicate',8,'p_spatial_predicate','parser.py',187),
  ('spatial_predicate -> DWITHIN LPAREN expression COMMA expression COMMA number COMMA UNITS RPAREN','spatial_predicate',10,'p_spatial_predicate','parser.py',188),
  ('spatial_predicate -> BEYOND LPAREN expression COMMA expression COMMA number COMMA UNITS RPAREN','spatial_predicate',10,'p_spatial_predicate','parser.py',189),
  ('spatial_predicate -> BBOX LPAREN expression COMMA number COMMA number COMMA number COMMA number RPAREN','spatial_predicate',12,'p_spatial_predicate','parser.py',190),
  ('spatial_predicate -> BBOX LPAREN expression COMMA number COMMA number COMMA number COMMA number COMMA QUOTED RPAREN','spatial_predicate',14,'p_spatial_predicate','parser.py',191),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','parser.py',210),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser.py',211),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',220),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',221),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser.py',222),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',223),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser.py',224),
  ('expression -> LBRACKET expression RBRACKET','expression',3,'p_expression','parser.py',225),
  ('expression -> GEOMETRY','expression',1,'p_expression','parser.py',226),
  ('expression -> ENVELOPE','expression',1,'p_expression','parser.py',227),
  ('expression -> attribute','expression',1,'p_expression','parser.py',228),
  ('expression -> QUOTED','expression',1,'p_expression','parser.py',229),
  ('expression -> INTEGER','expression',1,'p_expression','parser.py',230),
  ('expression -> FLOAT','expression',1,'p_expression','parser.py',231),
  ('number -> INTEGER','number',1,'p_number','parser.py',248),
  ('number -> FLOAT','number',1,'p_number','parser.py',249),
  ('attribute -> ATTRIBUTE','attribute',1,'p_attribute','parser.py',254),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',259),
]
