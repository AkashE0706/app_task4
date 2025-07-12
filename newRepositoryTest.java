package com.example.myapp;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import retrofit2.Response;
import com.example.myapp.network.ApiService;
import com.example.myapp.repository.Repository;
import org.mockito.Mockito;
import java.util.Collections;
import java.util.List;

public class RepositoryTest {
    private Repository repo;
    private ApiService service = Mockito.mock(ApiService.class);

    @Before
    public void setup() {
        repo = new Repository(service);
    }

    @Test
    public void testFetchData_success() throws Exception {
        List<?> dummy = Collections.emptyList();
        Mockito.when(service.getDataList().execute()).thenReturn(Response.success(dummy));

        // call and assert
        List<?> data = repo.fetchDataSync();
        assertNotNull(data);
        assertTrue(data.isEmpty());
    }
}
