<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;


/**
 * @OA\Info(
 *     version="1.0.0",
 *     title="Your API Name",
 *     description="A description of your API"
 * )
 * @OA\Server(
 *     description="Your server description",
 *     url="http://127.0.0.1:8000"
 * )
 * @OA\SecurityScheme(
 *     securityScheme="bearerAuth",
 *     type="http",
 *     scheme="bearer"
 * )
 * @OA\Schema(
 *     schema="PaginationMeta",
 *     title="Pagination Meta",
 *     description="Metadata for pagination",
 *     @OA\Property(property="current_page", type="integer", example=1),
 *     @OA\Property(property="from", type="integer", example=1),
 *     @OA\Property(property="last_page", type="integer", example=5),
 *     @OA\Property(property="path", type="string", example="http://127.0.0.1:8000/resource"),
 *     @OA\Property(property="per_page", type="integer", example=15),
 *     @OA\Property(property="to", type="integer", example=15),
 *     @OA\Property(property="total", type="integer", example=50)
 * )
 */
class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;
}
