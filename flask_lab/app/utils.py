from typing import Dict, Any, List

import pandas as pd


def dict_to_html(dict_objects: List[Dict[str, Any]]) -> str:
    df = pd.DataFrame(dict_objects)
    html = df.to_html(index=False, classes="stocktable", table_id="table1")
    html = html.replace('class="dataframe ', 'class="')
    return html
