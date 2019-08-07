#### Splunk Enterprise

5 Main functions:
1. **Index Data**\
  Collects data from virtually any source\
  Look at the data and how to process it. When a match is found, the data gets a source type as it's label.\
  Workers use the source type to break the data into single events. Which is then timestamped (identified and normalized to a consistent format)\
  These events are stored in **SPLUNK INDEX**
2. **Search and Investigate**\
  Splunk Search Language
  Run statistics
3. **Add Knowledge**\
  Labelling, add enrichment, normalize the data
4. **Monitor and Alert**\
  Automated alerts and respond with Action
5. **Report and Analyze**

MD can be available, accessible and usable to everyone in the organization


3 Main Processing Components:
1. **Indexer**\
  Processes incoming machine data, storing the results in Splunk Index as events\
  These events are organized in a set of directories by age (required organization for searching the data)
2. **Search Head**\
  Allows users to use the Splunk Search language to search the index data\
  Handles search requests from users and distributes the request to Indexers, which performs the actual searches on the data\
  Search head then consolidate and enriches the result from Indexers before returning to user\
  Tools - Dashboards, reports and visualizations
3. **Forwarder**\
  Splunk Enterprise instances that consumes data and forward it to the Indexers for processing\
  Reuire minimal resources and little impact on performance\
  They reside on the machines where the data originates\
  ** If WebServer is supposed to be monitored then Forwarder is installed on it which then forwards the data to the Indexer.\
  ** In most Splunk deployments, forwarders server as the Primary way data is supplied for indexing.
  
How does these components scale in deployments?
1. Splunk Instance Deployment
- Input, Parsing, Indexing and Searching
- Perfect for **Proof of concept**, **Personal use**, **Learning** and **small department-sized environments**
2. For Production environment - we would need to have multiple instances of Splunk enterprise components.
- Multiple forwarders, search heads and indexers/ cluster of indexers.


#### Quiz 2

1. A single-instance deployment of Splunk Enterprise handles:
Select all that apply.
- [x] Searching
- [x] Parsing
- [x] Input
- [x] Indexing

2. What are the three main processing components of Splunk?
Select all that apply.
- [x] Search Heads
- [x] Forwarders
- [x] Indexers
- [ ] Deployment Maker
- [ ] Distributors

3. Which function is not a part of a single instance deployment?
Select your answer.
- [ ] Parsing
- [ ] Searching
- [ ] Indexing
- [x] Clustering

4. Search requests are processed by the ___________.
Select your answer.
- [x] Indexers
- [ ] Forwarders
- [ ] Search Heads

5. In most Splunk deployments, ________ serve as the primary way data is supplied for indexing.
Select your answer.
- [x] Forwarders
- [ ] Search Heads
- [ ] Local Files
