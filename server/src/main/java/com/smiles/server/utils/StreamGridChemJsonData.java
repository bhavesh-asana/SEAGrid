package com.smiles.server.utils;

import org.bson.Document;

import java.util.List;
import java.util.stream.Collectors;

public class StreamGridChemJsonData {
    private final List<Document> listOfGridChemRecords;

    public StreamGridChemJsonData(List<Document> listOfGridChemRecords) {
        this.listOfGridChemRecords = listOfGridChemRecords;
    }

    public static StreamGridChemJsonData of(List<Document> listOfGridChemRecords){
        return new StreamGridChemJsonData(listOfGridChemRecords);
    }

    public String toJsonString(){
        return listOfGridChemRecords
            .stream()
            .map(Document::toJson)
            .collect(Collectors.joining(",", "{\"data\": [", "]}"));
    }
}