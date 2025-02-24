class System:

    def __init__(self):
        detailed_needs = """"
        Business Need: Global Retail Solutions (GRS) Data Warehouse

        Global Retail Solutions (GRS) is a multinational, omni-channel retail enterprise operating through brick-and-mortar stores, e-commerce platforms, and mobile applications. To drive data-informed decision-making and support both operational reporting and advanced analytics, GRS requires a robust and scalable data warehousing solution. The core objectives are:

        Comprehensive Sales and Transaction Tracking:

        Capture every sales transaction from multiple channels (in-store, online, mobile) with detailed line-item data including product information, pricing, discounts, taxes, and returns.
        Support real-time updates and historical analysis, enabling ad-hoc queries such as identifying seasonal trends and comparing performance across channels.
        Customer Demographics and Behavioral Analysis:

        Maintain detailed profiles including demographic details, purchase history, browsing behavior, loyalty program membership, and customer feedback.
        Enable segmentation and lifetime value analysis, so analysts can query questions like “Which customer segments show the highest repeat purchase rates?” or “How does customer behavior vary by region?”
        Inventory and Supply Chain Management:

        Track real-time inventory levels across multiple warehouses and retail outlets.
        Integrate supplier data, shipment tracking, order fulfillment metrics, and supplier performance statistics.
        Allow predictive analytics to forecast stock shortages and optimize replenishment cycles.
        Product Catalog and Hierarchical Organization:

        Create a detailed product catalog that captures product attributes, categories, subcategories, variants, and historical pricing.
        Support complex queries that correlate product performance with promotional campaigns and market trends.
        Digital Marketing and Social Media Integration:

        Integrate campaign performance data from digital channels, including click-through rates, conversion metrics, and social media sentiment analysis.
        Enable cross-channel marketing impact analysis, such as comparing promotional effectiveness across regions.
        Financial and Operational Insights:

        Aggregate revenue, cost, and profit data to provide financial dashboards that support quarterly forecasting and performance benchmarking.
        Include key performance indicators (KPIs) that link operational data (like inventory turnover and order fulfillment times) with financial outcomes.
        External Market Data and Competitive Intelligence:

        Integrate external data sources such as industry benchmarks, competitor pricing, and macroeconomic indicators.
        Support queries that compare GRS performance against market trends, enhancing strategic planning.
        The designed schema must be normalized for Online Analytical Processing (OLAP) and optimized for complex, cross-dimensional queries. It should also support natural language query interfaces, enabling non-technical analysts to ask questions like:

        “Which regions had the highest revenue growth in Q1, and what were the top-selling product categories?”
        “How have inventory levels fluctuated in response to recent marketing campaigns?”
        This comprehensive system should be flexible enough to accommodate new data sources over time, support incremental data loads, and ensure high performance and fault tolerance across a variety of DBMS platforms using JDBC connectors, with tailored SQL dialect adjustments for systems like Trino, Spark SQL, PostgreSQL, MS SQL Server, Oracle, and MySQL.
        """
