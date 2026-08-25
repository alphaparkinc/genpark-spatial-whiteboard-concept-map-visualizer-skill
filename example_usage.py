from client import SpatialWhiteboardConceptMapVisualizerClient

def main():
    client = SpatialWhiteboardConceptMapVisualizerClient()
    res = client.build_spatial_knowledge_whiteboard('Distributed Consensus Protocols (Raft vs Paxos vs PBFT)', 24)
    print('Whiteboard: ' + res['whiteboard_id'] + ' (' + res['domain'] + ')')
    print('Cards: ' + str(res['spatial_cards_placed_count']) + ' | Connected Edges: ' + str(res['concept_relationship_edges_connected']))
    print('Clusters: ' + ', '.join(res['visual_cluster_sections']))
    print('Board URL: ' + res['interactive_canvas_share_url'])

if __name__ == '__main__':
    main()
