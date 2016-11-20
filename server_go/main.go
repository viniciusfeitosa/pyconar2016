package main

import (
	"net/http"

	"encoding/json"
	"log"
	"time"
)

const port = ":8080"

// Speaker is the representation for the speaker entity
type Speaker struct {
	Name        string
	TalkTitle   string
	ConsultedAt string
}

func main() {
	http.HandleFunc("/pyconar", func(w http.ResponseWriter, r *http.Request) {
		speaker := Speaker{
			Name:        "Vinicius Pacheco",
			TalkTitle:   "Introducción al Gevent",
			ConsultedAt: time.Now().Format("02/01/2006 15:04:05"),
		}
		jsonBody, err := json.Marshal(speaker)
		if err != nil {
			log.Fatalln(err)
		}

		time.Sleep(1 * time.Second)
		w.Header().Set("Content-Type", "application/json; charset=utf-8")
		w.WriteHeader(http.StatusOK)
		w.Write(jsonBody)
	})

	log.Println("Start server on", port)
	http.ListenAndServe(port, nil)
}
