
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False)


df = pd.read_csv('Sales_cleaned.csv')


# Add a title and subheader to the app
st.title('Sales Analysis and Visualization')
st.write("-------------------------------------------")

st.image('image.jpeg')
st.markdown(""" According to the U.S. Census Bureau, the sales for technology in the USA in 2019 amounted to $1.4 trillion, a 3.4% increase from 2018. This analysis shows that the technology sector was one of the fastest-growing and most resilient industries in the country, despite the challenges posed by the trade war, the pandemic, and the economic slowdown. The main drivers of this growth were software, cloud services, e-commerce, and telecommunications, which accounted for more than half of the total sales.
""")
st.write("-------------------------------------------")

st.subheader('PROBLEMS')
# Problem 1
st.markdown("###### - What was the best month for sales? How much was earned that month?")

# Problem 2
st.markdown("###### - What city sold the most product?")

# Problem 3
st.markdown("###### - What time should we display advertisements to maximize likelihood of customer’s buying products?")

# Problem 4
st.markdown("###### - What Products are most often sold together?")

# Problem 5
st.markdown("###### - What product sold the most? Why do you think it did?")

st.write("-------------------------------------------")

# Sidebar for analysis selection
analysis_option = st.sidebar.selectbox('Select Analysis', [
    '---',  # Add the placeholder option "---"
    'Product Analysis',
    'Time Analysis',
    'Correlation Analysis'
])

# Check if the selected analysis option is not "---"
if analysis_option != '---':
     
    if analysis_option == 'Product Analysis':
        st.subheader('Product Analysis')
        
        # Create checkboxes for different product-related visualizations
        checkboxes = {
            "Most Popular Products": "show_popular_products",
            "Average Price and Total Revenue": "show_average_revenue",
            "City Counts": "show_city_counts",
            "Profit for each city": "show_profit_city",
            "profit for each day of the week": "show_profit_day",
        }
        
        selected_checkboxes = {}
        for label, variable_name in checkboxes.items():
            selected_checkboxes[variable_name] = st.sidebar.checkbox(label)
        
        if selected_checkboxes["show_popular_products"]:
            st.subheader('Most Popular Products')
            product_counts = df['Product'].value_counts().sort_values(ascending=False)
            fig = px.bar(x=product_counts.index, y=product_counts.values, color=product_counts.index ,title='Product Counts', labels={'x': 'Product', 'y': 'Count'})
            st.plotly_chart(fig)
        
        if selected_checkboxes["show_average_revenue"]:
            st.subheader('Average Price and Total Revenue')
            mean_prices = df.groupby('Product')['Price'].mean()
            fig_avg=px.bar(x=mean_prices.index, y=mean_prices.values, color=mean_prices.index ,title='Product and Price', labels={'x': 'Product', 'y': 'Price'})
            st.plotly_chart(fig_avg)
            total_revenue_by_product = df.groupby('Product')['TotalPrice'].sum().reset_index()

            total_revenue_by_product = df.groupby('Product')['profit'].sum().reset_index()
            #sort products by total revenue in descending order
            top_products = total_revenue_by_product.sort_values(by='profit', ascending=False)
            #visualize top products by total revenue
            fig=px.bar(top_products, x='Product', y='profit',color="Product", title='Top Products by Total Revenue')
            st.plotly_chart(fig)
        
        if selected_checkboxes["show_city_counts"]:
            st.subheader('City Counts')
            fig = px.bar(x=df['City'].value_counts().index, y=df['City'].value_counts().values, color=df['City'].value_counts().index ,title='City Counts', labels={'x': 'City', 'y': 'Count'})
            st.plotly_chart(fig)
        if selected_checkboxes['show_profit_city']:
            st.subheader('profit for each city')
            # calculate the profit for each city    
            total_revenue_by_city = df.groupby('City')['profit'].sum().reset_index()
            fig=px.bar(total_revenue_by_city, x='City', y='profit', color='City', title='Total Revenue by City')
            st.plotly_chart(fig)
        if selected_checkboxes['show_profit_day']:
            st.subheader('profit for each day of the week')
            # calculate the profit for each day of the week
            profit_by_day = df.groupby('Day')['profit'].sum().reset_index()
            #sorting 
            profit_by_day = profit_by_day.sort_values(by='profit', ascending=False)
            fig=px.bar(profit_by_day, x='Day', y='profit', color='Day', title='Total Revenue by Day')
            st.plotly_chart(fig)


    # Continue with other analysis options

    elif analysis_option == 'Time Analysis':
        st.subheader('Time Analysis')
        
        # Create checkboxes for different time-related visualizations
        show_year = st.sidebar.checkbox("Show Year Counts")
        show_month = st.sidebar.checkbox("Show Month Counts")
        show_day = st.sidebar.checkbox("Show Day Counts")
        show_hour = st.sidebar.checkbox("Show Hour Counts")
        show_timeofday = st.sidebar.checkbox("Show Time Of Day Counts")
        show_season = st.sidebar.checkbox("Show Season Counts")
        
        st.subheader('Sales Trends')
        # Add code for sales trends analysis and visualizations
        
        # Add your sales trends analysis code here
        
        st.subheader('Busiest Hours, Months, and Years')
        # Add code for busiest hours, months, and years analysis and visualizations
        
        if show_year:
            fig_year = px.bar(x=df['Year'].value_counts().index, y=df['Year'].value_counts().values, color=df['Year'].value_counts().index, title='Year Counts', labels={'x': 'Year', 'y': 'Count'})
            st.plotly_chart(fig_year)
        
        if show_month:
            fig_month = px.bar(x=df['Month_name'].value_counts().index, y=df['Month_name'].value_counts().values, color=df['Month_name'].value_counts().index, title='Month Counts', labels={'x': 'Month', 'y': 'Count'})
            st.plotly_chart(fig_month)
        
        if show_day:
            fig_day = px.bar(x=df['Day'].value_counts().index, y=df['Day'].value_counts().values, color=df['Day'].value_counts().index, title='Day Counts', labels={'x': 'Day', 'y': 'Count'})
            # Assuming you have already calculated the pivot table
            st.plotly_chart(fig_day)
            pivot_table_result = df.pivot_table(index='Day', values='TotalPrice', aggfunc='sum')
            # Display the pivot table result in your Streamlit app
            st.write("Total Sales by Day")
            st.write(pivot_table_result)
            fig = px.bar(x=pivot_table_result.index, y=pivot_table_result['TotalPrice'],color=pivot_table_result.index,
             labels={'x': 'Day', 'y': 'Total Sales'},
             title='Total Sales by Day')
            st.plotly_chart(fig)

        
        if show_hour:
            fig_hour = px.bar(x=df['hour'].value_counts().index, y=df['hour'].value_counts().values, color=df['hour'].value_counts().index, title='Hour Counts', labels={'x': 'Hour', 'y': 'Count'})
            st.plotly_chart(fig_hour)
        
        if show_timeofday:
            fig_timeofday = px.bar(x=df['TimeOfDay'].value_counts().index, y=df['TimeOfDay'].value_counts().values, color=df['TimeOfDay'].value_counts().index, title='TimeOfDay Counts', labels={'x': 'TimeOfDay', 'y': 'Count'})
            st.plotly_chart(fig_timeofday)
        
        if show_season:
            fig_season = px.bar(x=df['Season'].value_counts().index, y=df['Season'].value_counts().values, color=df['Season'].value_counts().index, title='Season Counts', labels={'x': 'Season', 'y': 'Count'})
            st.plotly_chart(fig_season)
        
    elif analysis_option == 'Correlation Analysis':
        st.subheader('Correlation Analysis')
        st.subheader('Correlation Heatmap')

        # Sample data (assuming you have a DataFrame named 'df')
        # Include only the relevant numerical columns for correlation analysis
        numerical_columns = ['Quantity Ordered', 'Price', 'TotalPrice']
        correlation_matrix = df[numerical_columns].corr()

        # Create a heatmap using seaborn
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Heatmap')
        st.pyplot()
        st.subheader('Product Popularity by City')
        # Group by 'Product' and 'City' and calculate sum of 'Quantity Ordered'
        product_city_group = df.groupby(['Product', 'City'])['Quantity Ordered'].sum().reset_index()

        # Pivot the table for better visualization
        pivot_table = product_city_group.pivot(index='Product', columns='City', values='Quantity Ordered')

        # Create a heatmap using seaborn
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='g')
        plt.title('Product Popularity by City')
        st.pyplot()
        st.subheader('Total Revenue by Product for Each City')
        # Calculate total revenue by product for each city
        total_revenue_by_product_city = df.groupby(['Product', 'City'])['profit'].sum().reset_index()
        top_revenue_city=total_revenue_by_product_city.sort_values(by='profit', ascending=False)
        # visualise the total revenue by product for each city
        px.bar(top_revenue_city, x='Product', y='profit', color='City', title='Total Revenue by Product for Each City')
        # make a heat map to display the total revenue by product for each city
        pivot_table = total_revenue_by_product_city.pivot(index='Product', columns='City', values='profit')
        pivot_table.head()
        # Create a heatmap using Seaborn
        plt.figure(figsize=(10, 6))
        plt.title('Total Revenue by Product for Each City')
        sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="coolwarm", cbar=True)
        plt.xlabel('City')
        plt.ylabel('Product')
        st.pyplot()
        st.subheader('Total Revenue by Product for Each Week Day')
        # Calculate total revenue by product for each day of the week
        total_revenue_by_product_day = df.groupby(['Product', 'Day'])['profit'].sum().reset_index()

        # # Visualize the total revenue by product for each week day using a bar chart
        # fig = px.bar(total_revenue_by_product_day, x='Product', y='profit', color='Day',
        #              title='Total Revenue by Product for Each Week Day',
        #              labels={'x': 'Product', 'y': 'Total Revenue'})
        # fig.show()

        # Create a pivot table for the heatmap
        pivot_table = total_revenue_by_product_day.pivot(index='Product', columns='Day', values='profit')

        # Create a heatmap using Seaborn
        plt.figure(figsize=(10, 6))
        plt.title('Total Revenue by Product for Each Week Day')
        sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="coolwarm", cbar=True)
        plt.xlabel('Day')
        plt.ylabel('Product')
        st.pyplot()




# Add other analysis options similarly

# Add a section to display filtered data based on user input
st.sidebar.subheader('Filtered Data')

# Add the placeholder option "---" to the list of product names
product_options = ['---'] + df['Product'].unique().tolist()

# Create a selectbox for product selection
selected_product = st.sidebar.selectbox('Select a Product:', product_options)

# Check if the selected product is not "---"
if selected_product != '---':
    filtered_df = df[df['Product'] == selected_product]
    st.write(filtered_df)

# Display the Streamlit app
st.sidebar.subheader('About')
st.sidebar.info("This app was created to analyze and visualize sales data.")

# If you want to add more interactivity, you can use Streamlit widgets
# For example, you can add interactive plots or charts using Plotly or Seaborn

# Run the app
if __name__ == '__main__':
    st.sidebar.subheader('Disclaimer')
    st.sidebar.warning("This app is for demonstration purposes only. Please do not use real data.")
