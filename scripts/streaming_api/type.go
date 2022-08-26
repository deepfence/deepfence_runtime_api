package main

type TopologyDiff struct {
	Edges struct {
		Add    interface{} `json:"add"`
		Remove interface{} `json:"remove"`
	} `json:"edges"`
	Metadata struct {
		ChildrenCount struct {
			_ struct {
				Hosts int64 `json:"hosts"`
			} `json:""`
		} `json:"children_count"`
		Connections string `json:"connections"`
	} `json:"metadata"`
	Nodes struct {
		Add []struct {
			ID                string `json:"id"`
			ImmediateParentID string `json:"immediate_parent_id"`
			Label             string `json:"label"`
			LabelMinor        string `json:"labelMinor"`
			Metadata          []struct {
				ID       string  `json:"id"`
				Label    string  `json:"label"`
				Priority float64 `json:"priority"`
				Value    string  `json:"value"`
			} `json:"metadata"`
			Rank  string `json:"rank"`
			Shape string `json:"shape"`
		} `json:"add"`
		Remove interface{} `json:"remove"`
		Update []struct {
			ID                string `json:"id"`
			ImmediateParentID string `json:"immediate_parent_id"`
			Label             string `json:"label"`
			LabelMinor        string `json:"labelMinor"`
			Metadata          []struct {
				DataType string  `json:"dataType"`
				ID       string  `json:"id"`
				Label    string  `json:"label"`
				Priority float64 `json:"priority"`
				Value    string  `json:"value"`
			} `json:"metadata"`
			Metrics []struct {
				Format   string      `json:"format"`
				Group    string      `json:"group"`
				ID       string      `json:"id"`
				Label    string      `json:"label"`
				Max      float64     `json:"max"`
				Min      float64     `json:"min"`
				Priority float64     `json:"priority"`
				Samples  interface{} `json:"samples"`
				URL      string      `json:"url"`
				Value    float64     `json:"value"`
			} `json:"metrics"`
			Parents []struct {
				ID         string `json:"id"`
				Label      string `json:"label"`
				TopologyID string `json:"topologyId"`
			} `json:"parents"`
			Rank  string `json:"rank"`
			Shape string `json:"shape"`
		} `json:"update"`
	} `json:"nodes"`
	Reset bool `json:"reset"`
}
