import streamlit  as st
st.header(" welcome to chamarajanagara")
button=st.button("GRT RESULT")
if button==True:
   table="""<table border="1">
<th> regno </th>
<th> name</th>
<th> sem </th>
<th> pms</th>
<th> s_and_a</th>
    <th>c_s</th>
    <th>caeg</th>
    <th>m_and_a</th>
    <th>total</th>
        <th>result</th>
<tr>
    <td>130CS21003</td><td>	AISHWARYA M</td><td>	2</td><td>	11</td>	<td>32</td>	<td>35</td>	<td>20</td>	<td>27</td>	<td>326</td>	<td>FAIL</td></tr>
    <td>130CS21005</td><td>AMITH G S</td><td>	2</td></td><td>	35	</td><td>36</td>	<td>37</td>	<td>29</td>	<td>34</td>	<td>419</td>	<td>Distinction</td>
    </table>"""
   st.markdown(table,unsafe_allow_html=True)
st.container()
