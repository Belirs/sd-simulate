from typing import Dict, List

current_scale = 1.0
last_scale = None
debug_mode = False
xml_type = None
loaded_svg_content = None
MIN_WIDTH = 1
MIN_HEIGHT = 1
current_image = None
transition_trace = []
state_stack = []
is_svg_updated = False
hints_visible = False
current_state: Dict[str, List[str]] = {"active": [], "remembered": []}
initial_state_key = None
transitions = {}
original_width = None
original_height = None
svg_file_path = None
svg_rainbow_file_path = None
transition_trace_label = None
transitions_file_path = None
show_parent_highlight = True
analysis_results_text = None
analysis_results_visible = False
full_content = None
