package de.tu_darmstadt.systems;

import org.apache.bookkeeper.client.LedgerHandle;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;

public class AsyncContext {
    private final List<CompletableFuture<Long>> onGoingRequests;

    public AsyncContext() {
        this.onGoingRequests = new ArrayList<>();
    }

    public void append(LedgerHandle ledgerHandle, byte[] data) {
        onGoingRequests.add(ledgerHandle.appendAsync(data));
    }

    public List<Long> waitForAll() {
        CompletableFuture.allOf(onGoingRequests.toArray(new CompletableFuture[0])).join();
        return onGoingRequests.stream().map(CompletableFuture::join).collect(Collectors.toList());
    }
}
