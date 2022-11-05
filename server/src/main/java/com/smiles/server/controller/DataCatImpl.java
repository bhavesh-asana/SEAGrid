package com.smiles.server.controller;

import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.Struct;
import com.google.protobuf.util.JsonFormat;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.smiles.server.GetGridChemRequest;
import com.smiles.server.GridChemServiceGrpc;
import com.mongodb.client.MongoClient;
import com.smiles.server.utils.StreamJsonData;
import io.grpc.stub.StreamObserver;
import org.bson.Document;

import java.util.ArrayList;
import java.util.List;

public class DataCatImpl extends GridChemServiceGrpc.GridChemServiceImplBase {

    String uri = "mongodb://localhost:27017";
    String dbName = "datacat";
    String collectionName = "gridchembkJSON";
    MongoClient connect = MongoClients.create(uri);
    MongoDatabase dbCursor = connect.getDatabase(dbName);
    MongoCollection<Document> dataCursor = dbCursor.getCollection(collectionName);

    List<Document> listOfGridChemRecords = dataCursor.find().into(new ArrayList<>());

    @Override
    public void getData(GetGridChemRequest request, StreamObserver<Struct> responseObserver) {
        Struct.Builder gridChemstructBuilder = Struct.newBuilder();
        try {
            JsonFormat.parser()
                    .merge(StreamJsonData.of(listOfGridChemRecords).toJsonString(), gridChemstructBuilder);
        } catch (InvalidProtocolBufferException e) {
            throw new RuntimeException(e);
        }
        responseObserver.onNext(gridChemstructBuilder.build());
        responseObserver.onCompleted();
    }
}
