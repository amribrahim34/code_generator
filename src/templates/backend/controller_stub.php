<?php

namespace {namespace};

use App\Http\Controllers\Controller;
use App\Models\{model_name};
use App\Http\Requests\{request_class};
use App\Http\Resources\{resource_class};
use App\Repositories\Interfaces\{repository_interface};
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Resources\Json\ResourceCollection;

/**
 * @OA\Tag(
 *     name="{model_name}",
 *     description="{model_name} resource"
 * )
 */
class {class_name} extends Controller
{{
    protected {repository_interface} ${model_variable}Repository;

    public function __construct({repository_interface} ${model_variable}Repository)
    {{
        $this->{model_variable}Repository = ${model_variable}Repository;
    }}

    /**
     * @OA\Get(
     *     path="/{api_version}/{model_variable}s",
     *     summary="List {model_variable}s",
     *     tags={{"{model_name}"}},
     *     @OA\Response(response="200", description="Successful operation"),
     *     @OA\Response(response="401", description="Unauthenticated"),
     *     @OA\Response(response="403", description="Forbidden")
     * )
     */
    public function index({request_class} $request): ResourceCollection
    {{
        $items = $this->{model_variable}Repository->paginate($request->validated());
        return {resource_class}::collection($items);
    }}

    /**
     * @OA\Post(
     *     path="/{api_version}/{model_variable}s",
     *     summary="Create a new {model_variable}",
     *     tags={{"{model_name}"}},
     *     @OA\RequestBody(required=true, description="{model_name} object that needs to be added"),
     *     @OA\Response(response="201", description="Successful operation"),
     *     @OA\Response(response="401", description="Unauthenticated"),
     *     @OA\Response(response="403", description="Forbidden"),
     *     @OA\Response(response="422", description="Validation error")
     * )
     */
    public function store({request_class} $request): JsonResponse
    {{
        $item = $this->{model_variable}Repository->create($request->validated());
        return (new {resource_class}($item))
            ->response()
            ->setStatusCode(201)
            ->setData(['message' => __("{model_variable}.created_successfully")]);
    }}

    /**
     * @OA\Get(
     *     path="/{api_version}/{model_variable}s/{{id}}",
     *     summary="Get a {model_variable} by ID",
     *     tags={{"{model_name}"}},
     *     @OA\Parameter(name="id", in="path", required=true, description="ID of {model_variable} to return"),
     *     @OA\Response(response="200", description="Successful operation"),
     *     @OA\Response(response="401", description="Unauthenticated"),
     *     @OA\Response(response="403", description="Forbidden"),
     *     @OA\Response(response="404", description="{model_name} not found")
     * )
     */
    public function show(int $id): JsonResponse
    {{
        $item = $this->{model_variable}Repository->findOrFail($id);
        return (new {resource_class}($item))->response();
    }}

    /**
     * @OA\Put(
     *     path="/{api_version}/{model_variable}s/{{id}}",
     *     summary="Update an existing {model_variable}",
     *     tags={{"{model_name}"}},
     *     @OA\Parameter(name="id", in="path", required=true, description="ID of {model_variable} to update"),
     *     @OA\RequestBody(required=true, description="{model_name} object that needs to be updated"),
     *     @OA\Response(response="200", description="Successful operation"),
     *     @OA\Response(response="400", description="Invalid ID supplied"),
     *     @OA\Response(response="401", description="Unauthenticated"),
     *     @OA\Response(response="403", description="Forbidden"),
     *     @OA\Response(response="404", description="{model_name} not found"),
     *     @OA\Response(response="422", description="Validation error")
     * )
     */
    public function update({request_class} $request, int $id): JsonResponse
    {{
        $item = $this->{model_variable}Repository->update($id, $request->validated());
        return (new {resource_class}($item))
            ->response()
            ->setData(['message' => __("{model_variable}.updated_successfully")]);
    }}

    /**
     * @OA\Delete(
     *     path="/{api_version}/{model_variable}s/{{id}}",
     *     summary="Delete a {model_variable}",
     *     tags={{"{model_name}"}},
     *     @OA\Parameter(name="id", in="path", required=true, description="ID of {model_variable} to delete"),
     *     @OA\Response(response="200", description="Successful operation"),
     *     @OA\Response(response="401", description="Unauthenticated"),
     *     @OA\Response(response="403", description="Forbidden"),
     *     @OA\Response(response="404", description="{model_name} not found")
     * )
     */
    public function destroy(int $id): JsonResponse
    {{
        $this->{model_variable}Repository->delete($id);
        return response()->json(['message' => __("{model_variable}.deleted_successfully")], 200);
    }}
}}